from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Macbook Air 13 M1 2020", callback_data="First")
    keyboard_builder.button(text="Macbook Pro 14 M1 Pro 2021", callback_data="Second")
    keyboard_builder.button(text="Apple Macbook Pro 16 2019", callback_data="Third")
    keyboard_builder.button(
        text="Link",
        url="https://yandex.ru/maps/2/saint-petersburg/?ll=30.358218%2C60.005885&z=13",
    )
    keyboard_builder.button(text="Profile", url="https://t.me/AlnurTK")

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
