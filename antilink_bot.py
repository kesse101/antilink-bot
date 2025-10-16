from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import re
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

LINK_REGEX = re.compile(
    r"(https?://|t\.me/|www\.|telegram\.me/|bit\.ly|tinyurl\.com)",
    re.IGNORECASE
)

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and LINK_REGEX.search(message.text or ""):
        try:
            await message.delete()
            print(f"🧹 Deleted: {message.text}")
        except Exception as e:
            print(f"❌ Error deleting message: {e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links))
    print("🤖 Antilink Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
