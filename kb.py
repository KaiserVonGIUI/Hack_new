from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu_continue = [[InlineKeyboardButton(text="Продолжить", callback_data="continue_button")]]
menu_continue = InlineKeyboardMarkup(inline_keyboard=menu_continue)

menu_yd = [[InlineKeyboardButton(text="Да", callback_data="yes_button")],
           [InlineKeyboardButton(text="Нет", callback_data="no_button")]
           ]
menu_yd = InlineKeyboardMarkup(inline_keyboard=menu_yd)

menu_profil = [[InlineKeyboardButton(text="Профиль", callback_data="profile_view")], #+
               [InlineKeyboardButton(text="Магазин", callback_data="shop_page")], #+
               [InlineKeyboardButton(text="Баланс", callback_data="balance")], #+
               [InlineKeyboardButton(text="Передача валюты", callback_data="Valute_sharing")], #+
               [InlineKeyboardButton(text="Проверить заказы", callback_data="zakaz_view")]] #+
menu_profil = InlineKeyboardMarkup(inline_keyboard=menu_profil)

menu_profil1 = [[InlineKeyboardButton(text="Редактировать профиль", callback_data="profile_edit")],
               [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]]
menu_profil1 = InlineKeyboardMarkup(inline_keyboard=menu_profil1)

menu_balance = [[InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]]
menu_balance = InlineKeyboardMarkup(inline_keyboard=menu_balance)

button_korzina = [[InlineKeyboardButton(text="В корзину", callback_data="in_korzina")]]
button_korzina = InlineKeyboardMarkup(inline_keyboard=button_korzina)

button_back_korzina = [[InlineKeyboardButton(text="Назад", callback_data="iz_korzina")]]
button_back_korzina = InlineKeyboardMarkup(inline_keyboard=button_back_korzina)

menu_shop1 = [[InlineKeyboardButton(text="В корзину", callback_data="zakaz_oformlenie")],
               [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]]
menu_shop1 = InlineKeyboardMarkup(inline_keyboard=menu_shop1)

menu_shop2 = [[InlineKeyboardButton(text="Оплатить", callback_data="oplata")],
               [InlineKeyboardButton(text="Отменить заказ", callback_data="otmena")]]
menu_shop2 = InlineKeyboardMarkup(inline_keyboard=menu_shop2)

menu_shop3 = [[InlineKeyboardButton(text="Назад", callback_data="oplata")],
              [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]]
menu_shop3 = InlineKeyboardMarkup(inline_keyboard=menu_shop3)

button_vibor = [[InlineKeyboardButton(text="Выбрать", callback_data="vibor")]]
button_vibor = InlineKeyboardMarkup(inline_keyboard=button_vibor)

button_vibor1 = [[InlineKeyboardButton(text="Продлить заказ", callback_data="vibor1")]]
button_vibor1 = InlineKeyboardMarkup(inline_keyboard=button_vibor1)



menu_admin = [[InlineKeyboardButton(text="Посмотреть профиль пользователя", callback_data="profile_user_view")],
               [InlineKeyboardButton(text="Проверить статусы заказов", callback_data="zakaz_user_view")],
               [InlineKeyboardButton(text="Посмотреть список товаров", callback_data="shop_tovari_view")]]
menu_admin = InlineKeyboardMarkup(inline_keyboard=menu_admin)

button_vibor_admin1 = [[InlineKeyboardButton(text="Выбрать", callback_data="vibor1_admin")]]
button_vibor_admin1 = InlineKeyboardMarkup(inline_keyboard=button_vibor_admin1)

but_cont = [[InlineKeyboardButton(text="Продолжить", callback_data="continue")]]
but_cont = InlineKeyboardMarkup(inline_keyboard=but_cont)

but_cont1 = [[InlineKeyboardButton(text="Продолжить", callback_data="continue1")]]
but_cont1 = InlineKeyboardMarkup(inline_keyboard=but_cont1)

menu_admin2 = [[InlineKeyboardButton(text="Изменить фамилию пользователя", callback_data="admin_edit_name1")], #+
               [InlineKeyboardButton(text="Изменить имя пользователя", callback_data="admin_edit_name2")], #+
               [InlineKeyboardButton(text="Изменить отчество пользователя", callback_data="admin_edit_name3")], #+
               [InlineKeyboardButton(text="Изменить отдел пользователя", callback_data="admin_edit_otdel")], #+
               [InlineKeyboardButton(text="Изменить статус пользователя", callback_data="admin_edit_admin")],
               [InlineKeyboardButton(text="Изменить баланс пользователя", callback_data="admin_edit_bal")],
               [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
               ] #+
menu_admin2 = InlineKeyboardMarkup(inline_keyboard=menu_admin2)

button_nazad_admin1 = [[InlineKeyboardButton(text="Назад", callback_data="vibor1_admin")]]
button_nazad_admin1 = InlineKeyboardMarkup(inline_keyboard=button_nazad_admin1)

button_nazad_admin2 = [[InlineKeyboardButton(text="Назад", callback_data="vibor2_admin")]]
button_nazad_admin2 = InlineKeyboardMarkup(inline_keyboard=button_nazad_admin2)

button_nazad_admin3 = [[InlineKeyboardButton(text="Назад", callback_data="vibor3_admin")]]
button_nazad_admin3 = InlineKeyboardMarkup(inline_keyboard=button_nazad_admin3)

button_vibor_admin2 = [[InlineKeyboardButton(text="Изменить заказ", callback_data="vibor2_admin")]]
button_vibor_admin2 = InlineKeyboardMarkup(inline_keyboard=button_vibor_admin2)

menu_admin3 = [[InlineKeyboardButton(text="Изменить пункт получения", callback_data="admin_edit_punkt")], #+
               [InlineKeyboardButton(text="Изменить статус заказа", callback_data="admin_edit_status")], #+
               [InlineKeyboardButton(text="Изменить срок хранения", callback_data="admin_edit_srok")],
               [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
               ] #+
menu_admin3 = InlineKeyboardMarkup(inline_keyboard=menu_admin3)

add_tovar = [[InlineKeyboardButton(text="Добавить новый товар", callback_data="add_tovar")],
             [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
             ]
add_tovar = InlineKeyboardMarkup(inline_keyboard=add_tovar)

button_vibor_admin3 = [[InlineKeyboardButton(text="Изменить товар", callback_data="vibor3_admin")]]
button_vibor_admin3 = InlineKeyboardMarkup(inline_keyboard=button_vibor_admin3)

menu_admin4 = [[InlineKeyboardButton(text="Изменить название товара", callback_data="admin_edit_namet")], #+
               [InlineKeyboardButton(text="Изменить цену товара", callback_data="admin_edit_price")], #+
               [InlineKeyboardButton(text="Изменить изображение", callback_data="admin_edit_image")],
               [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
               ] #+
menu_admin4 = InlineKeyboardMarkup(inline_keyboard=menu_admin4)

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

