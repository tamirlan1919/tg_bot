from aiogram import Router
from .commands import router as commands_router
from .text import router as text_router


router = Router()
router.include_routers(commands_router, text_router)