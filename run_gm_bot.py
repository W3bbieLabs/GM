# --- module imports ---
# import schedule
import time
import os

# --- define welcome message ---
def welcome():
    message = "ready to start gm bot"
    os.system(f"echo --- {message} ---")

# --- setup job ---
def gm_bot():
    os.system("python3 /users/xyz/gm_bot/app.py")

# --- flow ---
welcome()
gm_bot = gm_bot()
# schedule.every().day.at("04:00").do(gm_bot)

# --- loop so always running ---
#while True:
    #schedule.run_pending()
    #time_sleep(1)
