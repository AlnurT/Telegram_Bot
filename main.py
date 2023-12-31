import asyncio
import logging
import sys
from datetime import datetime, timedelta

import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.filters.iscontact import IsTrueContact
from core.handlers import apsched, form
from core.handlers.basic import (
    command_start,
    get_hello,
    get_inline,
    get_location,
    get_photo,
)
from core.handlers.callback import select_macbook
from core.handlers.contact import get_fake_contact, get_true_contact
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.officehours import OfficeHoursMiddleware
from core.settings import settings
from core.utils.commands import set_commands
from core.utils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(836876955, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(836876955, text="Бот остановлен!")


async def create_pool():
    return await asyncpg.create_pool(
        user="postgres",
        password=settings.password.db_password,
        database="users",
        host="127.0.0.1",
        port=5432,
        command_timeout=60,
    )


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(settings.bots.bot_token, parse_mode=ParseMode.HTML)

    pool_connect = await create_pool()
    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        apsched.send_message_time,
        trigger="date",
        run_date=datetime.now() + timedelta(seconds=10),
        kwargs={"bot": bot},
    )
    scheduler.add_job(
        apsched.send_message_cron,
        trigger="cron",
        hour=datetime.now().hour,
        minute=datetime.now().minute + 1,
        start_date=datetime.now(),
        kwargs={"bot": bot},
    )
    scheduler.add_job(
        apsched.send_message_interval,
        trigger="interval",
        seconds=60,
        kwargs={"bot": bot},
    )
    scheduler.start()

    dp.message.middleware.register(CounterMiddleware())
    dp.message.middleware.register(OfficeHoursMiddleware())
    dp.update.middleware.register(DbSession(pool_connect))
    dp.update.middleware.register(SchedulerMiddleware(scheduler))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(form.get_form, Command(commands="form"))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
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
