from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv  # Add this import

load_dotenv()

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f'{message.from_user.full_name}, {message.from_user.id}')
