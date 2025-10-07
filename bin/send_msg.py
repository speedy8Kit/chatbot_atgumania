import asyncio
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

# Проверяем, что обязательные переменные установлены
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен. Проверьте файл .env")
if CHAT_ID:
    try:
        chat_id_int = int(CHAT_ID)
        print(f"CHAT_ID как число: {chat_id_int}")
        
        # Определяем тип чата по ID
        if str(chat_id_int).startswith('-100'):
            print("📢 Тип чата: Супергруппа/Канал")
        elif str(chat_id_int).startswith('-'):
            print("👥 Тип чата: Группа")
        else:
            print("💬 Тип чата: Личные сообщения")
            
    except ValueError:
        print(f"📛 CHAT_ID как username: {CHAT_ID}")
else:
    print("❌ CHAT_ID не установлен")


# Преобразуем CHAT_ID в int (если это числовой ID) или оставляем как строку (если username)
try:
    CHAT_ID = int(CHAT_ID)
except ValueError:
    pass

async def send_message_async(text):
    """Асинхронная функция для отправки сообщения"""
    bot = Bot(token=BOT_TOKEN)
    # await bot.send_message(chat_id=CHAT_ID, text="ТЫ ОТЖАЛСЯ СЕГОДНЯ?!?!")
    await bot.send_message(chat_id=CHAT_ID, text=text)
    print("✅ Сообщение отправлено!")


def main():
    """Основная функция"""
    print("🤖 Telegram Bot - Отправка сообщений")
    print("=" * 40)
    print(f"💬 Chat ID: {CHAT_ID}")
    print(f"🔐 Token: {'*' * len(BOT_TOKEN)}")
    print("=" * 40)
    
    asyncio.run(send_message_async("считаю до пяти"))
    for i in range(1, 6):
        asyncio.run(send_message_async(i))

if __name__ == "__main__":
    main()