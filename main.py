import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from core.handlers.basic import command_start
from core.settings import settings


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.message.register(command_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
