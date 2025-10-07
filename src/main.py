import os
import datetime
import schedule
import time
from telegram import Bot
from dotenv import load_dotenv

from check_params import check_env_vals
from config import BASE_CONFIG

# Загружаем переменные окружения из .env файла
BASE_CONFIG

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