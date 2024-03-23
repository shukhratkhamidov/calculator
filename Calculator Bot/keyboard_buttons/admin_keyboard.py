from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Reklama yuborish"),
        ],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

user_bot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni")
        ],
    ],
     resize_keyboard=True,
     input_field_placeholder="Foydalanuvchilar soni"
)


calc_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilimiz"),
            KeyboardButton(text="Biz haqimizda"),
            KeyboardButton(text="Admin"),
            KeyboardButton(text="Admin bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True,
)
