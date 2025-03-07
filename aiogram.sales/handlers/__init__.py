from aiogram import Dispatcher
from .users.start import router as start_router
from .users.help import router as help_router
from .admin.admin_commands import router as admin_commands_router

def setup(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(admin_commands_router)