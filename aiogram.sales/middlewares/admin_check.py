import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS

class AdminCheckMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable,
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Получаем user_id в зависимости от типа события
        user_id = event.from_user.id if isinstance(event, Message) else event.message.from_user.id
        
        if user_id not in ADMINS:
            logging.warning(f"Несанкционированная попытка доступа от пользователя {user_id}")
            
            if isinstance(event, Message):
                await event.answer(
                    "⛔️ Доступ запрещен!\n"
                    "Эта команда доступна только администраторам."
                )
            elif isinstance(event, CallbackQuery):
                await event.answer(
                    "⛔️ У вас нет прав администратора!",
                    show_alert=True
                )
            return
        
        try:
            # Добавляем информацию об админе в data
            data['is_admin'] = True
            data['admin_id'] = user_id
            
            # Продолжаем выполнение
            return await handler(event, data)
            
        except Exception as e:
            logging.error(f"Ошибка в админ-middleware: {e}")
            await event.answer("Произошла ошибка при обработке команды администратора")
            return
