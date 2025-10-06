import datetime
import schedule
import time
from telegram import Bot

# Вставь сюда токен, полученный от BotFather
BOT_TOKEN = 'твой_токен_сюда'

# Вставь сюда ID группового чата (можно получить отправив сообщение и получив ID с помощью бота @chatid_echo_bot)
CHAT_ID = -1001234567890  # пример ID группы (начинается с -100)

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