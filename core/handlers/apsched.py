from aiogram import Bot


async def send_message_time(bot: Bot):
    await bot.send_message(836876955, "После старта бота")


async def send_message_cron(bot: Bot):
    await bot.send_message(836876955, "В указанное время")


async def send_message_interval(bot: Bot):
    await bot.send_message(836876955, "Интервал в 1 мин")


async def send_message_middleware(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, "Middleware")
