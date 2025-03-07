import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS_ID", "").split(",") if admin_id]

API_KEY_DEEPSEEK = os.getenv("API_KEY_DEEPSEEK")

if __name__ == "__main__":
    print(BOT_TOKEN)
    print(ADMINS)
    print(API_KEY_DEEPSEEK)