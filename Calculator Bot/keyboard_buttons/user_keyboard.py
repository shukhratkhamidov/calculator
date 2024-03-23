from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder



builder3 = ReplyKeyboardBuilder()
# Qator usuli sizga aniq qator yaratish imkonini beradi
# bir yoki bir nechta tugmalardan. Masalan, birinchi qator
# ikkita tugmadan iborat bo'ladi ...
builder3.row(
    KeyboardButton(text="Manzil yuborish", request_location=True),
    KeyboardButton(text="Kontakt yuborish", request_contact=True)
)
