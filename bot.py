import asyncio
import json
import logging
import os
import random
from datetime import datetime

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Simple in-memory storage for notes
user_notes: dict[int, list[str]] = {}


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="About", callback_data="about"),
            InlineKeyboardButton(text="Help", callback_data="help"),
        ],
        [
            InlineKeyboardButton(text="My Notes", callback_data="notes"),
            InlineKeyboardButton(text="Random Quote", callback_data="quote"),
        ],
    ])
    await message.answer(
        f"Hello, {message.from_user.first_name}! I'm a multi-functional bot.\n\n"
        "Choose an option below or type /help to see all commands.",
        reply_markup=keyboard,
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "<b>Available Commands:</b>\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/note &lt;text&gt; - Save a note\n"
        "/notes - View all your notes\n"
        "/clear - Clear all your notes\n"
        "/quote - Get a random inspirational quote\n"
        "/weather &lt;city&gt; - Get weather info\n"
        "/time - Show current server time\n"
        "/dice - Roll a dice\n"
    )
    await message.answer(help_text, parse_mode="HTML")


@dp.message(Command("note"))
async def cmd_note(message: types.Message):
    text = message.text.removeprefix("/note").strip()
    if not text:
        await message.answer("Usage: /note <your note text>")
        return

    user_id = message.from_user.id
    if user_id not in user_notes:
        user_notes[user_id] = []
    user_notes[user_id].append(text)
    count = len(user_notes[user_id])
    await message.answer(f"Note saved! You have {count} note(s) total.")


@dp.message(Command("notes"))
async def cmd_notes(message: types.Message):
    user_id = message.from_user.id
    notes = user_notes.get(user_id, [])

    if not notes:
        await message.answer("You have no saved notes. Use /note <text> to add one.")
        return

    notes_text = "\n".join(f"{i+1}. {note}" for i, note in enumerate(notes))
    await message.answer(f"<b>Your Notes:</b>\n\n{notes_text}", parse_mode="HTML")


@dp.message(Command("clear"))
async def cmd_clear(message: types.Message):
    user_id = message.from_user.id
    count = len(user_notes.get(user_id, []))
    user_notes[user_id] = []
    await message.answer(f"Cleared {count} note(s).")


@dp.message(Command("quote"))
async def cmd_quote(message: types.Message):
    quotes = [
        "The only way to do great work is to love what you do. — Steve Jobs",
        "Code is like humor. When you have to explain it, it's bad. — Cory House",
        "First, solve the problem. Then, write the code. — John Johnson",
        "Talk is cheap. Show me the code. — Linus Torvalds",
        "Programs must be written for people to read. — Harold Abelson",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
        "The best error message is the one that never shows up. — Thomas Fuchs",
        "Simplicity is the soul of efficiency. — Austin Freeman",
    ]
    await message.answer(f"💡 {random.choice(quotes)}")


@dp.message(Command("time"))
async def cmd_time(message: types.Message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await message.answer(f"Current server time: {now}")


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice()


@dp.callback_query(F.data == "about")
async def callback_about(callback: types.CallbackQuery):
    await callback.message.answer(
        "I'm a Telegram bot built with Python and Aiogram 3.\n"
        "I can save notes, show quotes, and more!"
    )
    await callback.answer()


@dp.callback_query(F.data == "help")
async def callback_help(callback: types.CallbackQuery):
    await cmd_help(callback.message)
    await callback.answer()


@dp.callback_query(F.data == "notes")
async def callback_notes(callback: types.CallbackQuery):
    callback.message.from_user = callback.from_user
    await cmd_notes(callback.message)
    await callback.answer()


@dp.callback_query(F.data == "quote")
async def callback_quote(callback: types.CallbackQuery):
    await cmd_quote(callback.message)
    await callback.answer()


@dp.message()
async def echo(message: types.Message):
    await message.answer(
        "I don't understand that command. Type /help to see available commands."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
