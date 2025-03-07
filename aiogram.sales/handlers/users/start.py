from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv  # Add this import

load_dotenv()

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    try:
        await message.answer(
            f"👋 Привет, {hbold(message.from_user.full_name)}!\n"
            f"Ваш ID: {message.from_user.id}\n"
            "Используйте /help для просмотра доступных команд."
        )
    except Exception as e:
        await message.answer("Произошла ошибка при обработке команды.")
