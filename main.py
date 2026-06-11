import os
import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "7722150910:AAHiNWB3fPpznTbFbVx-N2BOT3ajgTp6RVA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
