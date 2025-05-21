from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Терапевт"),
    KeyboardButton(text="Невролог")],
    [KeyboardButton(text="Окулист"),
    KeyboardButton(text="Травматолог")]
])

tera = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='9:30')],
    [KeyboardButton(text='10:00')],
    [KeyboardButton(text='10:30')],
    [KeyboardButton(text='11:00')]
])
neur = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='9:30' )],
    [KeyboardButton(text='10:30')],
    [KeyboardButton(text='11:30')],
    [KeyboardButton(text='13:00')]
])
oku = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='11:30')],
    [KeyboardButton(text='13:00')],
    [KeyboardButton(text='14:30')],
    [KeyboardButton(text='15:00')]
])
travm = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='9:30')],
    [KeyboardButton(text='10:00')],
    [KeyboardButton(text='10:30')],
    [KeyboardButton(text='11:00')]
])