from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from app.models import db, User
from app.utils import calculate_credits

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username
    age = 25  # Example age
    new_user = User(username=username, age=age, credits=calculate_credits(age))
    db.session.add(new_user)
    db.session.commit()

    button = KeyboardButton("Open App")
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    update.message.reply_text('Welcome to the Mini App!', reply_markup=keyboard)

def referral(update: Update, context: CallbackContext) -> None:
    user = User.query.filter_by(username=update.message.from_user.username).first()
    user.credits += 143
    user.referrals += 1
    db.session.commit()
    update.message.reply_text('You have earned 143 $PEPEZI for referring a friend!')

def leaderboard(update: Update, context: CallbackContext) -> None:
    users = User.query.order_by(User.referrals.desc()).all()
    leaderboard = "\n".join([f"{user.username}: {user.referrals} referrals" for user in users])
    update.message.reply_text(f"Leaderboard:\n{leaderboard}")
