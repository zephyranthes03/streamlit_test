import asyncio
import os
from aiogram import Bot, Dispatcher, types

# 봇 토큰을 여기에 입력하세요
API_TOKEN = os.getenv("BOT_TOKEN")

# 봇 설정
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def get_user_info(user_id: int):
    try:
        user_info = await bot.get_chat(user_id)
        return user_info
    except Exception as e:
        print(f"Error: {e}")
        return None

async def main():
    user_id = 6010115501  # 정보를 조회할 사용자 ID를 여기에 입력하세요
    user_info = await get_user_info(user_id)

    if user_info:
        print(f"User ID: {user_info.id}")
        print(f"First Name: {user_info.first_name}")
        print(f"Last Name: {user_info.last_name}")
        print(f"Username: {user_info.username}")
        print(f"Type: {user_info.type}")
    else:
        print("Unable to fetch user information.")

if __name__ == '__main__':
    asyncio.run(main())