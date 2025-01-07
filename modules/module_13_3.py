from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7502709533:AAEk4K1EJ981x8c6L_veAG8jgJqhdH73Rzo"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я бот!')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)