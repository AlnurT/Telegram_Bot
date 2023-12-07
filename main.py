import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from core.handlers.basic import command_start
from core.settings import settings


async def start_bot(bot: Bot):
    await bot.send_message(836876955, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(836876955, text="Бот остановлен!")


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(command_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
