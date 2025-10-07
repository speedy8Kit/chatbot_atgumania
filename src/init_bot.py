import os
from telegram import Bot
from config import BASE_CONFIG

def init_bot():
    
    bot = Bot(token=BASE_CONFIG.bot_config)
    return bot
