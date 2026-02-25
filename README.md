# Telegram Bot

A multi-functional Telegram bot built with Python and Aiogram 3. Features note-taking, inspirational quotes, inline keyboards, and more.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Aiogram](https://img.shields.io/badge/Aiogram-3.15-green)

## Features

- **Notes system** — save, view, and clear personal notes
- **Inline keyboards** — interactive buttons for quick navigation
- **Random quotes** — inspirational programming quotes
- **Dice rolling** — Telegram's built-in dice animation
- **Server time** — display current server time
- **Echo handler** — guides users to available commands

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot with inline keyboard |
| `/help` | Show all available commands |
| `/note <text>` | Save a new note |
| `/notes` | View all saved notes |
| `/clear` | Clear all notes |
| `/quote` | Get a random programming quote |
| `/time` | Show current server time |
| `/dice` | Roll a dice |

## Setup

1. Clone the repo:
```bash
git clone https://github.com/armenvart777/telegram-bot.git
cd telegram-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file from the example:
```bash
cp .env.example .env
```

4. Get a bot token from [@BotFather](https://t.me/BotFather) and add it to `.env`

5. Run:
```bash
python bot.py
```

## Tech Stack

- **Language:** Python 3.10+
- **Framework:** Aiogram 3
- **Storage:** In-memory (dict)

## License

MIT
