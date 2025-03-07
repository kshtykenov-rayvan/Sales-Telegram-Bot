from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    CallbackQuery
)
from middlewares.admin_check import AdminCheckMiddleware

router = Router()
router.message.middleware(AdminCheckMiddleware())

@router.message(Command("admin"))
async def admin_panel(message: Message):
    # Создаем веб-приложение
    web_app = WebAppInfo(url="https://your-webapp-url.com")
    
    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 Админ-панель", 
                    web_app=web_app
                )
            ],
            [
                InlineKeyboardButton(
                    text="📈 Статистика", 
                    callback_data="admin_stats"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Рассылка", 
                    callback_data="admin_broadcast"
                )
            ]
        ]
    )

    await message.answer("На команду /admin я отвечаю вот таким сообщением.\n", reply_markup=keyboard)

@router.callback_query(F.data == "admin_stats")
async def show_stats(callback: CallbackQuery):
    await callback.answer("Загрузка статистики...")
    await callback.message.answer("📊 Статистика:\nВ разработке...")

@router.callback_query(F.data == "admin_broadcast")
async def start_broadcast(callback: CallbackQuery):
    await callback.answer("Открываю форму рассылки...")
    await callback.message.answer("📨 Рассылка:\nВ разработке...")
