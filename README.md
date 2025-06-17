Интерфейс на FastAPI для взаимодействия с GREEN-API. Реализованы методы:

-getSettings
-getStateInstance
-sendMessage`
-sendFileByUrl`

Всё доступно через HTML-страницу



## Функционал

- Ввод `idInstance` и `ApiTokenInstance` один раз
- Все методы доступны в одном окне
- Ответ отображается справа от форм
- Поддержка отправки сообщений и файлов в WhatsApp

---

## Стек

- **FastAPI** – backend API
- **httpx** – HTTP-клиент для работы с GREEN-API
- **HTML + JS (fetch)** – frontend без перезагрузки
- **Uvicorn** – запуск приложения

---

## Установка

```bash
git clone https://github.com/malikushq/green_api.git
cd green_api
pip install -r requirements.txt
