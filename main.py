import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart

from core.filters.iscontact import IsTrueContact
from core.handlers.basic import (
    command_start,
    get_hello,
    get_inline,
    get_location,
    get_photo,
)
from core.handlers.callback import select_macbook
from core.handlers.contact import get_fake_contact, get_true_contact
from core.settings import settings
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(836876955, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(836876955, text="Бот остановлен!")


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_location, F.location)
    dp.message.register(get_inline, Command("inline"))
    dp.callback_query.register(select_macbook, F.data)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == "Привет")
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(command_start, CommandStart())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
