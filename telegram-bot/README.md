# Telegram Bot (Python)

Минимальный Telegram-бот на `python-telegram-bot` с polling.

## Что умеет

- `/start` — приветствие
- `/help` — список команд
- `/id` — показать chat id
- `/prototype` — отправить файл `business-navigator-product-prototype.html` из корня проекта
- Эхо для обычных текстовых сообщений

## Быстрый запуск

```bash
cd /Applications/Диплом/telegram-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Впиши токен в `.env`:

```env
BOT_TOKEN=123456:ABCDEF...
```

Запуск:

```bash
python bot.py
```

## Как получить токен

1. Открой `@BotFather` в Telegram.
2. Выполни `/newbot`.
3. Скопируй токен и вставь в `.env`.
