from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('help'))
async def help(message: Message):
    await message.answer(f"На команду /help я отвечаю вот таким сообщением.\n")