from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *


api = "7502709533:AAHzwDixJqmtbP2x8ln_zvxgwEfb-AlnocQ"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


get_all_products()


start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Формулы')
button3 = KeyboardButton('Купить')
start_menu.add(button1)
start_menu.add(button2)
start_menu.add(button3)


buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Product1', callback_data= 'product_buying'),
        InlineKeyboardButton(text='Product2', callback_data= 'product_buying'),
        InlineKeyboardButton(text='Product3', callback_data= 'product_buying'),
        InlineKeyboardButton(text='Product4', callback_data= 'product_buying')
        ]
    ],
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in get_all_products():
        product_id, title, description, price = product
        with open(f'productX.jpg', 'rb') as photo:
            await message.answer_photo(
                photo=photo,
                caption = f'Название: {title} | Описание: {description} | Цена: {price}')
    await message.answer('Выберите продукт:', reply_markup=buy_menu)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация!')


@dp.message_handler(text="Формулы")
async def get_formulas(message):
    await message.answer(
        'Для женщин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161;'
        'Для мужчин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5.'
    )


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите совй рост.')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес.')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = int(data['weight']) * 10 + int(data['growth']) * 6.25 - int(data['age']) * 5 + 5
    await message.answer(f'Calories: {calories}.')
    await state.finish()


@dp.message_handler(text="start")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=start_menu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

connection.close()
