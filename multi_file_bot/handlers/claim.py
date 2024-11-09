from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

claim_router = Router()

@claim_router.message(Command("claim"))
async def command_claim_handler(message: Message, command: CommandObject):
    # arguments = message.get_args()
    # await message.reply(arguments)
    await message.answer(f"Hello Command Claim, <b>{message.from_user.full_name}!</b> {message.from_user.id}")
