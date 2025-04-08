from telegram import Update
from telegram.ext import ContextTypes
from functools import wraps
import time
from config import Config

def restricted_admin(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != Config.ADMIN_ID:
            await update.message.reply_text("⚠️ Unauthorized access!")
            return
        return await func(update, context)
    return wrapper

def rate_limit(limit=3, period=60):
    def decorator(func):
        @wraps(func)
        async def wrapped(update, context, *args, **kwargs):
            user_data = context.user_data
            now = time.time()
            
            timestamps = user_data.get('timestamps', [])
            timestamps = [t for t in timestamps if now - t < period]
            
            if len(timestamps) >= limit:
                await update.effective_message.reply_text(
                    "🚫 Too many requests. Please wait."
                )
                return
            
            timestamps.append(now)
            user_data['timestamps'] = timestamps
            return await func(update, context, *args, **kwargs)
        return wrapped
    return decorator
