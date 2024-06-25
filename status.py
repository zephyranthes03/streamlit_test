import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

# 봇 토큰을 여기에 입력하세요
API_TOKEN = os.getenv("BOT_TOKEN")
API_TOKEN ="7439567925:AAGjEEXzSFO_DwDlfaQ6uZ8jGKy25sx8rKI"
API_TOKEN = "7146884682:AAGlkBMN1AAwcLsuQQ50_7IQd5R5EvSZZ0I"
# 봇 토큰을 여기에 입력하세요

# 봇 및 디스패처 설정
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# /start 명령어 처리
@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.answer("Hello! Send me a user ID to check their status.")

# 사용자 ID 입력받아 상태 확인
@router.message(F.text)
async def check_user_status(message: Message):
    try:
        user_id = int(message.text)
        user_info = await bot.get_chat(user_id)
        print(user_info, flush=True)

        # 사용자 정보 추출
        first_name = user_info.first_name
        last_name = user_info.last_name
        username = user_info.username
        user_id = user_info.id
        
        # 결과 메시지 구성
        user_details = f"User details:\n- ID: {user_id}\n- First name: {first_name}\n- Last name: {last_name}\n- Username: {username}"
        
        last_seen = user_info.last_seen #user_info.status
        await message.answer(f"User status: {last_seen}")
    except ValueError:
        await message.answer("Please provide a valid user ID.")
    except Exception as e:
        await message.answer(f"An error occurred: {e}")

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

