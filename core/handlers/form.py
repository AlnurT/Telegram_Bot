from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.utils.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(
        f"{message.from_user.first_name}, "
        f"начинаем заполнять анкету. Введите своё имя"
    )
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Твоё имя: {message.text}\n" f"Теперь введите фамилию")
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f"Твоя фамилия: {message.text}\n" f"Теперь введите возраст")
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f"Твой возраст: {message.text}")
    context_data = await state.get_data()
    await message.answer(f"Данные: {str(context_data)}")
    name = context_data.get("name")
    last_name = context_data.get("last_name")
    data_user = (
        f"Вот твои данные:\n"
        f"Имя - {name}\n"
        f"Фамилия - {last_name}\n"
        f"Возраст - {message.text}"
    )

    await message.answer(data_user)
    await state.clear()
