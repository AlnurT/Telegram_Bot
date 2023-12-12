from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from core.keyboards.inline import get_inline_keyboard
from core.keyboards.reply import get_reply_keyboard


async def get_inline(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}. Показываю инлайн кнопки!",
        reply_markup=get_inline_keyboard(),
    )


async def command_start(message: Message):
    await message.answer(
        f"Привет, {hbold(message.from_user.first_name)}!",
        reply_markup=get_reply_keyboard(),
    )


async def get_location(message: Message):
    await message.answer(
        f"Ты отправил локацию!\r\a"
        f"{message.location.latitude}\r\a{message.location.longitude}"
    )


async def get_photo(message: Message, bot: Bot):
    await message.answer("Картинка отправлена!")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "photo.jpg")


async def get_hello(message: Message):
    await message.answer("И тебе привет!")
