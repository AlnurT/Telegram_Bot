from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold


async def command_start(message: Message):
    await message.answer(f"Привет, {hbold(message.from_user.first_name)}!")


async def get_photo(message: Message, bot: Bot):
    await message.answer("Картинка отправлена!")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "photo.jpg")
