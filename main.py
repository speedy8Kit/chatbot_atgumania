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


bot = Bot(token=BOT_TOKEN)

def days_to_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    delta = new_year - today
    return delta.days

def pushup_reminder():
    days_left = days_to_new_year()
    pushups = 100 - days_left
    if pushups < 0:
        pushups = 0
    message = f"Привет! Сегодня нужно сделать {pushups} отжиманий. Осталось {days_left} дней до Нового года!"
    bot.send_message(chat_id=CHAT_ID, text=message)

# Запускаем функцию раз в день в 9 утра
schedule.every().day.at("09:00").do(pushup_reminder)

print("Бот для ежедневных напоминаний запущен!")
while True:
    schedule.run_pending()
    time.sleep(60)