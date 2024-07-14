from app import app
from app.bot import run_bot
from threading import Thread

if __name__ == "__main__":
    # Start the Telegram bot in a separate thread
    bot_thread = Thread(target=run_bot)
    bot_thread.start()
    
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
