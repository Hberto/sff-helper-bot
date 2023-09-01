import logging
from telegram import *
from telegram.ext import *
from requests import *
from ui.utils import *
from typing import List, Union

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# first test with the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Menu", reply_markup=reply_markup)
        #await context.bot.send_message(chat_id=update.effective_chat.id, text="Peep peep peep ich habe euch alle lieb!", reply_markup=ReplyKeyboardMarkup(buttons))

# unknown commands warning
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this command doesn't exit.")


async def keyboard_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "Liebe":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Peep peep peep ich habe euch alle lieb!")
    
    if query.data == "Webseite":
       await update.callback_query.answer(text="Link to our website: https://studentsforfuture-hamburg.de/")

    if query.data == "Ultimate":
       await update.callback_query.answer(text="Link to our intern Q&A Pad. It includes all the information you need: https://pad.fridaysforfuture.is/p/SFF_Struktur_Infos")


if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()

    start_handler = CommandHandler('start', start)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(unknown_handler)
    application.add_handler(CallbackQueryHandler(keyboard_callback))
    application.run_polling()
