import logging
from telegram.ext import Application
from config import Config
from database import db
from handlers import user_handlers, admin_handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main() -> None:
    application = Application.builder().token(Config.TOKEN).build()
    
    # Register handlers
    application.add_handlers([
        user_handlers.conv_handler,
        admin_handlers.admin_handler,
        user_handlers.payment_handler,
        user_handlers.support_handler,
        user_handlers.referral_handler
    ])
    
    # Error handling
    application.add_error_handler(error_handler)
    
    # Start polling
    application.run_polling()

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error("Exception while handling update:", exc_info=context.error)

if __name__ == "__main__":
    main()
