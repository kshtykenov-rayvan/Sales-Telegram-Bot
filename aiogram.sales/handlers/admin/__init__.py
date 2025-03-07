from . import admin_commands

__all__ = ['admin_commands']

def setup(dp):
    dp.include_router(admin_commands.router)