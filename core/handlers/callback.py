from aiogram.types import CallbackQuery


async def select_macbook(call: CallbackQuery):
    await call.message.answer(f"Вы выбрали - {call.data} Macbook")
    await call.answer()
