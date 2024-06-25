import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from datetime import datetime

# 봇 토큰을 여기에 입력하세요
API_TOKEN = 'YOUR_BOT_API_TOKEN'
API_TOKEN = "7146884682:AAGlkBMN1AAwcLsuQQ50_7IQd5R5EvSZZ0I"

# 봇 설정
bot = Bot(token=API_TOKEN)

# 디스패처 및 라우터 설정
dp = Dispatcher()
router = Router()

# SQLite 데이터베이스 설정
conn = sqlite3.connect('user_activity.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_activity (
        user_id INTEGER PRIMARY KEY,
        last_interaction TIMESTAMP
    )
''')
conn.commit()

# /start 명령어 처리
@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.answer("Hello! Send me a message and I will record the interaction time.")

# 사용자 메시지 기록
@router.message(F.text)
async def record_user_interaction(message: Message):
    user_id = message.from_user.id
    interaction_time = message.date

    # 데이터베이스에 기록
    cursor.execute('''
        INSERT INTO user_activity (user_id, last_interaction)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET last_interaction=excluded.last_interaction
    ''', (user_id, interaction_time))
    conn.commit()

    await message.answer(f"Recorded interaction at {interaction_time}")

# 비활성 시간 계산 및 확인
@router.message(Command(commands=['inactive']))
async def check_inactive_time(message: Message):
    user_id = message.from_user.id

    cursor.execute('SELECT last_interaction FROM user_activity WHERE user_id=?', (user_id,))
    result = cursor.fetchone()

    if result:
        last_interaction_time = datetime.fromisoformat(result[0])
        current_time = datetime.utcnow()
        inactive_duration = current_time - last_interaction_time

        await message.answer(f"You have been inactive for {inactive_duration}")
    else:
        await message.answer("No interaction record found.")

# 라우터를 디스패처에 등록
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
