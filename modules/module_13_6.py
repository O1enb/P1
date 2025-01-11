from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = "api"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Рассчитать', callback_data= 'calories'),
        InlineKeyboardButton(text='Формулы', callback_data= 'formulas')
        ]
    ],
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация!')


@dp.message_handler(text="start")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=start_menu)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer(
        'Для женщин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161; Для мужчин: (10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5.'
    )
    await call.answer()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


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


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
