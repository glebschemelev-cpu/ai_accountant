import logging
import os
from pathlib import Path

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROTOTYPE_FILE = PROJECT_ROOT / "business-navigator-product-prototype.html"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    await update.message.reply_text(
        "Привет! Я Telegram-бот.\n\n"
        "Команды:\n"
        "/help — список команд\n"
        "/id — твой chat id\n"
        "/prototype — отправить HTML-прототип\n"
        "\nИли просто напиши сообщение, я отвечу эхом."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start\n"
        "/help\n"
        "/id\n"
        "/prototype"
    )


async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.effective_chat:
        return
    await update.message.reply_text(f"Твой chat id: {update.effective_chat.id}")


async def prototype_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    if not PROTOTYPE_FILE.exists():
        await update.message.reply_text("Файл прототипа не найден.")
        return
    with PROTOTYPE_FILE.open("rb") as file:
        await update.message.reply_document(
            document=file,
            filename=PROTOTYPE_FILE.name,
            caption="Вот актуальный HTML-прототип.",
        )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return
    await update.message.reply_text(f"Эхо: {update.message.text}")


def get_token() -> str:
    load_dotenv()
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Не задан BOT_TOKEN. Создай .env и укажи токен.")
    return token


def main() -> None:
    token = get_token()
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(CommandHandler("prototype", prototype_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
