from aiogram.types import Message
from aiogram.utils.markdown import hbold


async def command_start(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.first_name)}!")
