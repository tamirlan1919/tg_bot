from aiogram import Bot, Dispatcher
import logging
from config import TOKEN
from handlers import Router
from database.models import create_table_users


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(TOKEN) #Соеденение с тг серверами и нашим ботом
    dp = Dispatcher() #Он ловит любой update
    dp.include_routers(Router)
    await dp.start_polling(bot) #Начинаем опрос бота, чтобы получать обновления


if __name__ == '__main__':
    import asyncio
    create_table_users()
    asyncio.run(main()) #Запускаем асинхронную функцию mainwww
