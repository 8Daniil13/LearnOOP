import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message


def get_token() -> str:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN is not set. Create a .env file or export BOT_TOKEN in your shell."
        )
    return token


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Привет! Я эхо-бот. Отправь мне сообщение — я повторю.")


@dp.message(F.text)
async def echo(message: Message) -> None:
    await message.answer(message.text)


async def main() -> None:
    bot = Bot(token=get_token())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
