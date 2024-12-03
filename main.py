import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards as kb
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Обработчик команды /dynamic
@dp.message(Command(commands=['dynamic']))
async def send_dynamic_keyboard(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=kb.get_show_more_keyboard())


# Обработчик нажатия на инлайн-кнопки
@dp.callback_query(lambda callback_query: callback_query.data in ['show_more', 'option_1', 'option_2'])
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == 'show_more':
        # Заменяем кнопку на "Опция 1" и "Опция 2"
        await callback_query.message.edit_reply_markup(reply_markup=kb.get_options_keyboard())
    elif callback_query.data == 'option_1':
        # Отправляем сообщение о выборе "Опция 1"
        await callback_query.message.answer("Вы выбрали Опция 1")
    elif callback_query.data == 'option_2':
        # Отправляем сообщение о выборе "Опция 2"
        await callback_query.message.answer("Вы выбрали Опция 2")


@dp.message(Command('links'))
async def link(message: Message):
    await message.reply(f'Привет, вот ссылки на ресурсы,{message.from_user.first_name}',
                        reply_markup=kb.inline_keyboard_test)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /links \n /dinamic')


# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)
    await message.answer("Выберите и нажмите одну из кнопок ниже:", reply_markup=kb.main)


# Обработчик нажатия кнопки "Привет"
@dp.message(lambda message: message.text == "Привет")
async def greet_user(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


# Обработчик нажатия кнопки "Пока"
@dp.message(lambda message: message.text == "Пока")
async def farewell_user(message: types.Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
