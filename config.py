import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("BOT_TOKEN", "7959293982:AAGXTbVR6sBGFtb4BRd0YkZLO2VHMAkx1R4")
    ADMIN_ID = int(os.getenv("ADMIN_ID", 5645032505))
    TRC20_ADDRESS = os.getenv("TRC20_ADDRESS", "TXYZ1234567890abcdefghijklmnopqrstuvw")
    REFERRAL_BONUS = 0.10
    PREMIUM_PRICES = {3: 8.0, 6: 13.0, 12: 18.0}
    MIN_TOPUP = 8.0
    DB_PATH = os.getenv("DB_PATH", "premium_bot.db")
    SUPPORT_TIMEOUT = 1200  # 20 minutes
