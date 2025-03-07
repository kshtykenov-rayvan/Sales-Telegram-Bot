from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('help'))
async def help(message: Message):
    help_text = """
🤖 Bot Commands Help:
/start - Start the bot
/help - Show this help message
/products - View available products
/cart - View your shopping cart
/orders - View your order history
"""
    await message.answer(help_text)