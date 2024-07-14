from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN
from app.handlers import start, referral, leaderboard

updater = Updater(TOKEN)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("referral", referral))
dp.add_handler(CommandHandler("leaderboard", leaderboard))

def run_bot():
    updater.start_polling()
    updater.idle()
