from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

papers = [
    InlineKeyboardButton("1", callback_data="paper_1"),
    InlineKeyboardButton("2", callback_data="paper_2"),
    InlineKeyboardButton("3", callback_data="paper_3"),
    InlineKeyboardButton("4", callback_data="paper_4"),
    InlineKeyboardButton("🏘 Bosh Sahifa🏘", callback_data="paper_home")
]

button = InlineKeyboardMarkup(row_width=2)
button.add(*papers)

_main = [
    InlineKeyboardButton("🍃 Konspekt Yozish ✍️", callback_data="paper_getpaper"),
    InlineKeyboardButton("👨🏻‍💻 Developer 👨🏻‍💻", callback_data="paper_dev")
]

main = InlineKeyboardMarkup(row_width=1)
main.add(*_main)

_home = [
    InlineKeyboardButton("🏘 Bosh Sahifa🏘", callback_data="paper_home")
]

home = InlineKeyboardMarkup(row_width=1)
home.add(*_home)
