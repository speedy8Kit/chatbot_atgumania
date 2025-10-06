import os
import datetime
import schedule
import time
from telegram import Bot
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем значения из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
DAILY_TIME = os.getenv('DAILY_TIME', '09:00')
MAX_PUSHUPS = int(os.getenv('MAX_PUSHUPS', '100')) 

# Проверяем, что обязательные переменные установлены
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен. Проверьте файл .env")
if not CHAT_ID:
    raise ValueError("❌ CHAT_ID не установлен. Проверьте файл .env")

# Преобразуем CHAT_ID в int (если это числовой ID) или оставляем как строку (если username)
try:
    CHAT_ID = int(CHAT_ID)
except ValueError:
    pass  # Оставляем как строку (для username)




    
if __name__ == "__main__":
    message = f"Привет!"
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)