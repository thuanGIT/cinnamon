# Q&A Discord Bot

## Description

Many a time, students are looking for a quick answer to questions related to due date, TA emails, and lab dates. The majority is still confused in where to get these pieces of information and some have to wait days for an email reply from TAs. Hence, why not build a bot that is available anytime for such questions? There comes the inspiration for Cinnamon.

Cinnamon is built as implementatin for quick Q & A sessions for PHYS122 Labs W2020. Users can invoke a Q & A sessions via built-in commands. Furthermore, cinnamon can be invoked to save FAQs in data base for preferences to other students.

## Tools

- Cinnamon is built with Discord.py package as the backend.
- Database is managed by MongoDB. To interact with MongoDB, we use Pymongo as the API wrapper.
- For hosting the bot, we run workers in Heroku dynos.

## Test it out

- Clone this repo: `git clone https://github.com/thuanGIT/cinnamon.git`
- Creat a virtual environment with **venv (Python 3)** or **env (Python 2)**: `python3 -m venv cinnamon`.
- Install dependencies: `pip install -r requirements.txt` (Run this at your project root).
- Use **dotenv** package to load environment variable from .env file: Remove the comment sign in load_dotenv().
- Set up discord application:
  - Create a discord channel to host the bot.
  - Create a discord application in [Discord Developer Portal](https://discord.com/developers/applications). Make sure to add Discord bot.
  - Copy the application token to TOKEN variable in .env.
  - Invite the bot to your server with OAuth2 URL Generator (Choose Bot).
- Run on local host: `python3 main.py`. Have fun!

Note: Run `#help` to see available commands to users!
