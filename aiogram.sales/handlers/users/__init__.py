from . import help
from . import start

__all__ = ['help', 'start']

def setup(dp):
    dp.include_router(help.router)
    dp.include_router(start.router)