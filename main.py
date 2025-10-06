import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import schedule
import time
import asyncio
from datetime import datetime, time as dt_time
import threading

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Глобальная переменная для хранения числа
current_number = 0

# Токен вашего бота (получите у @BotFather)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Привет! Я буду отправлять тебе сообщение каждый день с увеличивающимся числом. "
        "Первое сообщение будет отправлено завтра утром."
    )

async def send_daily_message(context: ContextTypes.DEFAULT_TYPE):
    """Функция для отправки ежедневного сообщения"""
    global current_number
    
    current_number += 1
    message = f"День #{current_number}\nСегодняшнее число: {current_number}\nДата: {datetime.now().strftime('%d.%m.%Y')}"
    
    # Отправляем сообщение всем пользователям, которые запустили бота
    # В реальном боте нужно хранить chat_id пользователей в базе данных
    try:
        # Здесь нужно получить chat_id из базы данных
        # Для примера используем фиксированный chat_id (замените на свой)
        chat_id = "YOUR_CHAT_ID_HERE"
        await context.bot.send_message(chat_id=chat_id, text=message)
        print(f"Сообщение отправлено: {message}")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

def schedule_checker():
    """Функция для проверки расписания в отдельном потоке"""
    while True:
        schedule.run_pending()
        time.sleep(1)

async def main():
    """Основная функция"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    
    # Настраиваем расписание
    # Отправка каждый день в 9:00 утра
    schedule.every().day.at("09:00").do(
        lambda: asyncio.create_task(send_daily_message(application))
    )
    
    # Запускаем проверку расписания в отдельном потоке
    schedule_thread = threading.Thread(target=schedule_checker, daemon=True)
    schedule_thread.start()
    
    # Запускаем бота
    print("Бот запущен...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())