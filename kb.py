from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu_continue = [[InlineKeyboardButton(text="Продолжить", callback_data="continue_button")]]
menu_continue = InlineKeyboardMarkup(inline_keyboard=menu_continue)

menu_yd = [[InlineKeyboardButton(text="Да", callback_data="yes_button")],
           [InlineKeyboardButton(text="Нет", callback_data="no_button")]
           ]
menu_yd = InlineKeyboardMarkup(inline_keyboard=menu_yd)

menu_profil = [[InlineKeyboardButton(text="Профиль", callback_data="profile_view")],
               [InlineKeyboardButton(text="Магазин", callback_data="shop_page")],
               [InlineKeyboardButton(text="Баланс", callback_data="balance")],
               [InlineKeyboardButton(text="Передача валюты", callback_data="Valute_sharing")],
               [InlineKeyboardButton(text="Проверить заказы", callback_data="zakaz_view")]]

""" menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])"""

