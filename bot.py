from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5955169114:AAGQyh9qOk6g9Mrbh5U7HUR8WUB0plNsNyI")

API_ID = int(os.environ.get("API_ID", "22113928"))

API_HASH = os.environ.get("API_HASH", "3c8c3c99870e5f4fd1f237f9431d870e")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
