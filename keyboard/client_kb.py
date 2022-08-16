from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = KeyboardButton("/start")
quiz = KeyboardButton("/quiz")
play = KeyboardButton('play')

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
start_markup.row(start, quiz, play)

