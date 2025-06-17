from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import JSONResponse 

import httpx

app = FastAPI()

@app.post("/get_settings")
async def get_settings(id_instance: str = Form(...), token: str = Form(...)):
    url = f"https://api.green-api.com/waInstance{id_instance}/getSettings/{token}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    try:
        json_data = response.json()
    except Exception:
        json_data = {
            "status_code": response.status_code,
            "error": "Invalid JSON",
            "raw": response.text
        }
    return JSONResponse(content=json_data)


@app.post("/get_state_instance")
async def get_state_instance(id_instance: str = Form(...), token: str = Form(...)):
    url = f"https://api.green-api.com/waInstance{id_instance}/getStateInstance/{token}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    try:
        json_data = response.json()
    except Exception:
        json_data = {
            "status_code": response.status_code,
            "error": "Invalid JSON",
            "raw": response.text
        }
    return JSONResponse(content=json_data)

@app.post("/send_message")
async def send_message(id_instance: str = Form(...),token: str = Form(...),chatId: str = Form(...),message: str = Form(...)):
    url = f"https://api.green-api.com/waInstance{id_instance}/sendMessage/{token}"
    payload = {
        "chatId": chatId,
        "message": message
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    try:
        json_data = response.json()
    except Exception:
        json_data = {
            "status_code": response.status_code,
            "error": "Invalid JSON",
            "raw": response.text
        }
    return JSONResponse(content=json_data)

@app.post("/send_file_by_url")
async def send_file_by_url(id_instance: str = Form(...),token: str = Form(...),chatId: str = Form(...),url_file: str = Form(...),file_name: str = Form(...)):
    url = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{token}"
    payload = {
        "chatId": chatId,
        "urlFile": url_file,
        "fileName": file_name
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    try:
        json_data = response.json()
    except Exception:
        json_data = {
            "status_code": response.status_code,
            "error": "Invalid JSON",
            "raw": response.text
        }
    return JSONResponse(content=json_data)
    
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
