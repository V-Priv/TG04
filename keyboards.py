from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://news.google.com/home?hl=ru&gl=RU&ceid=RU:ru')],
   [InlineKeyboardButton(text="Музыка", url='https://radiopotok.ru/pop')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/')]
])


# Создаем инлайн-кнопку "Показать больше"
def get_show_more_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    button_show_more = InlineKeyboardButton(text="Показать больше", callback_data="show_more")
    keyboard_builder.add(button_show_more)
    return keyboard_builder.as_markup()

# Создаем инлайн-кнопки "Опция 1" и "Опция 2"
def get_options_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    button_option_1 = InlineKeyboardButton(text="Опция 1", callback_data="option_1")
    button_option_2 = InlineKeyboardButton(text="Опция 2", callback_data="option_2")
    keyboard_builder.add(button_option_1, button_option_2)
    return keyboard_builder.as_markup()


test = ["Опция 1", "Опция 2"]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()
