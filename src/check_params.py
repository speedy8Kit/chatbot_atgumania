"""Файл содержит функции для проверки наличия всех переменных"""
import os


def check_env_vals():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    
    DAILY_TIME = os.getenv('DAILY_TIME', '09:00')
    MAX_PUSHUPS = int(os.getenv('MAX_PUSHUPS', '100')) 
    
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
        raise ValueError("❌ CHAT_ID не установлен")
    # TODO скорее всего id чатов с которыми работает нужно хранить в отдельном файле