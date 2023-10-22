from aiogram import F, Router, Dispatcher, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from aiogram.types import Message, InputFile, BufferedInputFile, URLInputFile
from aiogram.enums.parse_mode import ParseMode
import config
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

import config
import kb
import text
import sqlite3

id_polzovatelya = -1
korzina = []
id_tov = -1
itog_price = 0
id_zakaz = -1
fl1 = State()
fl2 = State()
id_1 = -1
flag_prodlenia = False
afl1 = State()
def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


profiles = sqlite3.connect('profiles.db')
cursor1 = profiles.cursor()

cursor1.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_tg INTEGER NOT NULL,
name1 TEXT NOT NULL,
name2 TEXT NOT NULL,
name3 TEXT NOT NULL,
otdel TEXT NOT NULL,
admin INT NOT NULL,
balance INTEGER NOT NULL)''')


profiles.commit()

shop_base = sqlite3.connect('shop_base.db')
cursor2 = shop_base.cursor()

cursor2.execute("""CREATE TABLE IF NOT EXISTS Shop_base ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price INTEGER NOT NULL, picture BLOB NOT NULL)""")

shop_base.commit()



zakaz_base = sqlite3.connect('zakaz_base.db')
cursor3 = zakaz_base.cursor()

cursor3.execute('''
CREATE TABLE IF NOT EXISTS Zakaz_base (
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_user INTEGER NOT NULL,
price INTEGER NOT NULL,
punkt TEXT NOT NULL,
status TEXT NOT NULL,
srok TEXT NOT NULL,
vopros BLOB NOT NULL)
''')

zakaz_base.commit()

router = Router()

class Tovar:
    name = "",
    price = 0,
    image = None

class Tovar1(StatesGroup):
    test234 = State()
    name = State()
    price = State()
    image = State()

class ClasS(StatesGroup):
    a1 = State()
    a2 = State()
    a3 = State()
    a4 = State()
    a5 = State()
    a6 = State()
    a7 = State()
    a8 = State()
    a9 = State()
    a10 = State()
    a11 = State()
    a12 = State()
    a13 = State()
    a14 = State()
    a15 = State()
    a16 = State()
    a17 = State()

class Profil:
    id_tg = 0,
    name1 = "",
    name2 = "",
    name3 = "",
    otdel = "",
    admin = 0,
    bal = 0


class Profile(StatesGroup):
    test123 = State()
    name1 = State()
    name2 = State()
    name3 = State()
    otdel = State()
    admin = State()



global name1
global name2
global name3
global otdel



@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text.greet)
    await msg.answer(text.name1)
    await state.set_state(Profile.test123)


@router.message(F.text, Profile.test123)
async def vod_name1(msg: Message, state: FSMContext):
    Profil.name1 = msg.text
    Profil.id_tg = msg.from_user.id
    await state.set_state(Profile.name1)
    await msg.answer(text.name2)


@router.message(Profile.name1, F.text)
async def vod_name2(msg: Message, state: FSMContext):
    Profil.name2 = msg.text
    print(Profil.name2)
    await state.set_state(Profile.name2)
    await msg.answer(text.name3)


@router.message(Profile.name2, F.text)
async def vod_name2(msg: Message, state: FSMContext):
    Profil.name3 = msg.text
    print(Profil.name3)
    await state.set_state(Profile.name3)
    await msg.answer(text.otdel)


@router.message(Profile.name3, F.text)
async def vod_name3(msg: Message, state: FSMContext):
    Profil.otdel = msg.text
    print(Profil.otdel)
    await state.set_state(Profile.otdel)
    await msg.answer(text.admin)


@router.message(Profile.otdel, F.text)
async def vod_name3(msg: Message, state: FSMContext):
    admin_text = msg.text
    if admin_text == "нет":
        Profil.admin = 0
    else:
        if admin_text == "test_code":
            Profil.admin = 1
        else:
            Profil.admin = 0
            await msg.answer(text.admin1)
    await state.set_state(Profile.admin)
    await msg.answer("")
    await state.set_state(Profile.admin)
    Profil.bal = 0
    cursor1.execute('INSERT INTO Users VALUES(1, ?, ?, ?, ?, ?, ?, ?)',
                    (str(Profil.id_tg), str(Profil.name1), str(Profil.name2), str(Profil.name3), str(Profil.otdel), str(Profil.admin), str(Profil.bal)))

@router.message(Profile.admin, F.text)
async def start_avtorisovaniy(msg: types.CallbackQuery):
    Profil.id_tg = msg.from_user.id

    id_1 = msg.chat.id
    print(id_1)
    cursor1.execute('SELECT * FROM Users WHERE name1=?', (str(Profil.name1),))
    row = cursor1.fetchall()
    for users1 in row:
        Profil.id_tg = users1[1]
        Profil.name1 = users1[2]
        Profil.name2 = users1[3]
        Profil.name3 = users1[4]
        Profil.otdel = users1[5]
        Profil.admin = users1[6]
        Profil.bal = users1[7]
        print(Profil.admin)

    await msg.answer(text.welcome, reply_markup=kb.menu_balance)

if Profil.admin == 0:
    @router.callback_query(F.data == "main_menu")
    async def start_polzovatel(msg: types.CallbackQuery):
        await msg.message.answer(f"Добро пожаловать, {Profil.name2} {Profil.name3}! Выберите необходимое действие", reply_markup=kb.menu_profil)

    @router.callback_query(F.data == "Valute_sharing")
    async def valute_sharing(msg: types.CallbackQuery):
        await msg.message.answer("Выберите получателя:")
        cursor1.execute('SELECT id, name1, name2, name3 FROM Users WHERE admin=?', (int(0), ))
        polzovateli = cursor1.fetchall()

        for row in polzovateli:
            await msg.message.answer(f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\n", reply_markup=kb.button_vibor)
            global id_polzovatelya
            id_polzovatelya = row[0]

        await msg.message.answer("", reply_markup=kb.menu_balance)

    @router.callback_query(F.data == "vibor")
    async def vibor_polzovatelya(msg: types.CallbackQuery, state: FSMContext):
        cursor1.execute('SELECT name1, name2, name3 FROM Users WHERE id=?', (int(id_polzovatelya), ))
        polzovateli = cursor1.fetchall()
        await msg.message.answer(f"Фамилия: {polzovateli[1]}\nИмя: {polzovateli[2]}\nОтчество: {polzovateli[3]}\n")
        await msg.message.answer("Введите сумму перевода")
        await state.set_state(fl1)

    @router.message(fl1, F.text)
    async def perevod_polzovatelu(msg: Message):
        summa_perevoda = int(msg.text)
        global id_polzovatelya
        if summa_perevoda <= Profil.bal:
            cursor1.execute('SELECT bal FROM Users WHERE id=?', (int(id_polzovatelya),))
            row = cursor1.fetchall()
            for polzovatel in row:
                global bal_1
                bal_1 = polzovatel[0] + summa_perevoda
                cursor1.execute('UPDATE Users SET balance = ? WHERE id = ?', (int(polzovatel[0]), int(id_polzovatelya)))
                profiles.commit()
                Profil.bal = Profil.bal - summa_perevoda
                cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (int(Profil.bal), int(Profil.id_tg)))
                await msg.answer("Перевод успешно выполнен!", reply_markup=kb.menu_balance)
        else:
            await msg.answer("Недостаточно средств на балансе!", kb.menu_balance)


    @router.callback_query(F.data == "zakaz_view")
    async def zakaz_view(msg: types.CallbackQuery):
        cursor3.execute('SELECT * FROM Zakaz_base WHERE id_user=?', (int(Profil.id_tg), ))
        zakazi = cursor3.fetchall()
        global id_zakaz
        global flag_prodlenia
        for zakaz in zakazi:
            await msg.message.answer(f"ID заказа: {zakaz[0]}\nСумма заказа: {zakaz[2]}\nПункт выдачи: {zakaz[3]}\nСтатус заказа: {zakaz[4]}\nСрок хранения: {zakaz[5]}\nБыл ли продлен срок хранения:: {zakaz[6]}\n", reply_markup=kb.button_vibor1)
            id_zakaz = zakaz[0]
            flag_prodlenia = zakaz[6]
        await msg.message.answer("", reply_markup=kb.menu_balance)

    @router.callback_query(F.data == "vibor1")
    async def zakaz_prodlit(msg: types.CallbackQuery, state: FSMContext):
        cursor3.execute('SELECT srok, vopros FROM Zakaz_base WHERE id=?', (int(id_zakaz), ))
        zakaz = cursor3.fetchall()
        if flag_prodlenia == False:
            await msg.message.answer("Введите дату крайнего срока получения заказа. Повторно продлить заказ нельзя. Если Вы не получите заказ до назначенного срока, заказ будет отменен администраторами")
            await state.set_state(fl2)
        else:
            await msg.message.answer("Заказ уже был продлен. Повторное продление невозможно", reply_markup=kb.menu_balance)

    @router.message(fl2, F.text)
    async def vvod_dati(msg: Message):
        date = msg.text
        cursor3.execute('UPDATE Zakaz_base SET srok = ? WHERE id = ?', (str(date), int(id_zakaz)))
        zakaz_base.commit()
        await msg.message.answer("Срок хранения заказа успешно продлен!", reply_markup=kb.menu_balance)


    @router.callback_query(F.data == "balance") #просмотр баланса
    async def view_balance(msg: types.CallbackQuery):
        await msg.message.answer(f"Ваш баланс равен: {Profil.bal}", reply_markup=kb.menu_balance)

    @router.callback_query(F.data == "shop_page")
    @router.callback_query(F.data == "iz_korzina")
    async def shop(msg: types.CallbackQuery):
        cursor2.execute('SELECT * FROM Shop_base')
        results = cursor2.fetchall()

        for row in results:
            await msg.message.answer(f"Наименование: {row[1]}\nID: {row[0]}\n")
            photo = InputFile(row[3])
            await bot.send_photo(photo=photo)
            await msg.message.answer(f"Цена: {row[2]}\n", reply_markup=kb.button_korzina)
            global  id_tov
            id_tov = row[0]

        await msg.message.answer("Меню", reply_markup=kb.menu_shop1)

    @router.callback_query(F.data == "zakaz_oformlenie")
    async def korzina_oformlenie(msg: types.CallbackQuery):
        for i in korzina:
            cursor2.execute('SELECT * FROM Shop_base WHERE id=?', (int(korzina[i]), ))
            result = cursor2.fetchall()
            await msg.message.answer(f"Наименование: {result[1]}\nЦена: {result[2]}")
            global itog_price
            itog_price = itog_price + result[2]
        await msg.message.answer(f"Итого: {itog_price}", reply_markup=kb.menu_shop2)

    @router.callback_query(F.data == "oplata")
    async def oplata(msg: types.CallbackQuery):
        global  itog_price
        if itog_price <= Profil.bal:
            Profil.bal = Profile.bal - itog_price
            cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (int(Profil.bal), int(Profil.id_tg)))
            profiles.commit()
            cursor1.execute('SELECT id_tg FROM Users WHER admin=?', (int(1), ))
            admins = cursor1.fetchall()
            for admin in admins:
                await bot.send_message(admins[admin], f"Новый заказ от пользователя {Profil.id_tg}: {Profil.name1} {Profil.name2} {Profil.name3} на сумму {itog_price}")
            korzina.clear()
            await msg.message.answer("Оплата успешна!\nОтслеживать статус заказа вы можете в соответствующем разделе!", reply_markup=kb.menu_balance)
        else:
            await msg.message.answer("Недостаточно средств на балансе!", reply_markup=kb.menu_shop3)


    @router.callback_query(F.data == "otmena")
    async def otmena_zakaz(msg: types.CallbackQuery):
        korzina.clear()
        await msg.message.answer("Заказ отменен!", reply_markup=kb.menu_balance)

    @router.callback_query(F.data == "in_korzina")
    async def in_korzina(msg: types.CallbackQuery):
        korzina.append(id_tov)
        await msg.message.answer(text.in_korzina, reply_markup=kb.button_back_korzina)

    @router.callback_query(F.data == "profile_view") #просмотр профиля
    async def profile_view(msg: types.CallbackQuery):
        await msg.message.answer(f"Фамилия: {Profil.name1}\nИмя: {Profil.name2}\nОтчество: {Profil.name3}\nОтдел: {Profil.otdel}\nАдминистратор: нет", reply_markup=kb.menu_profil1)

    @router.callback_query(F.data == "profile_edit") #редактирование профиля
    async def edit_profile(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer(text.name1)
        await state.set_state(Profile.test123)


    @router.message(Profile.test123, F.text)
    async def vod_name1(msg: Message, state: FSMContext):
        Profil.name1 = msg.text
        await state.set_state(Profile.name1)
        await msg.answer(text.name2)


    @router.message(Profile.name1, F.text)
    async def vod_name2(msg: Message, state: FSMContext):
        Profil.name2 = msg.text
        print(Profil.name2)
        await state.set_state(Profile.name2)
        await msg.answer(text.name3)


    @router.message(Profile.name2, F.text)
    async def vod_name2(msg: Message, state: FSMContext):
        Profil.name3 = msg.text
        print(Profil.name3)
        await state.set_state(Profile.name3)
        await msg.answer(text.otdel)


    @router.message(Profile.name3, F.text)
    async def vod_name3(msg: Message, state: FSMContext):
        Profil.otdel = msg.text
        print(Profil.otdel)
        await state.set_state(Profile.otdel)
        await msg.answer(text.admin)


    @router.message(Profile.otdel, F.text)
    async def vod_name3(msg: Message, state: FSMContext):
        admin_text = msg.text
        if admin_text == "нет":
            Profil.admin = 0
        else:
            if admin_text == "test_code":
                Profil.admin = 1
            else:
                await msg.answer(text.admin1)
        await state.set_state(Profile.admin)
        cursor1.execute('UPDATE Users SET name1 = ? WHERE id_tg = ?', (str(Profil.name1), int(Profil.id_tg)))
        cursor1.execute('UPDATE Users SET name2 = ? WHERE id_tg = ?', (str(Profil.name2), int(Profil.id_tg)))
        cursor1.execute('UPDATE Users SET name3 = ? WHERE id_tg = ?', (str(Profil.name3), int(Profil.id_tg)))
        cursor1.execute('UPDATE Users SET otdel = ? WHERE id_tg = ?', (str(Profil.otdel), int(Profil.id_tg)))
        cursor1.execute('UPDATE Users SET admin = ? WHERE id_tg = ?', (int(Profil.admin), int(Profil.id_tg)))
        cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (int(Profil.balance), int(Profil.id_tg)))

        profiles.commit()
else:
    @router.callback_query(F.data == "main_menu") #оснвное меню
    async def start_admin(msg: types.CallbackQuery):
        await msg.message.answer(f"Добро пожаловать, администратор {Profil.name2} {Profil.name3}! Выберите необходимое действие", reply_markup=kb.menu_admin)


    @router.callback_query(F.data == "profile_user_view")
    async def user_profile_edit(msg: types.CallbackQuery):
        await msg.message.answer("Выберите пользователя:")
        cursor1.execute('SELECT * FROM Users WHERE admin=0')
        row = cursor1.fetchall()


        global id_polzovatelya
        id_polzovatelya = row[0][0]
        print(id_polzovatelya)
        await msg.message.answer(f"Фамилия: {row[2]}\nИмя: {row[3]}\nОтчество: {row[4]}\n", reply_markup=kb.button_vibor_admin1)
        await msg.message.answer("", reply_markup=kb.menu_balance)


    @router.callback_query(F.data == "vibor1_admin")
    async def vibor_polzovatelya_admin(msg: types.CallbackQuery):
        cursor1.execute('SELECT * FROM Users WHERE id=?', (str(id_polzovatelya), ))
        row = cursor1.fetchall()
        for polzovatel in row:
            await msg.message.answer(f"ID: {polzovatel[0]}\nФамилия: {polzovatel[2]}\nИмя: {polzovatel[3]}\nОтчество: {polzovatel[4]}\nОтдел: {polzovatel[5]}\nАдминистратор: нет\nБаланс: {polzovatel[7]}",reply_markup=kb.menu_admin2)

    @router.callback_query(F.data == "admin_edit_name1")
    async def edit1(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите новую фамилию пользователя:")
        await state.set_state(ClasS.a7)

    @router.message(ClasS.a7, F.text)
    async def vvod_edit1(msg: Message):
        text_admin = msg.text
        cursor1.execute('UPDATE Users SET name1=? WHERE id=?', (str(text_admin), int(id_polzovatelya)))
        print(id_polzovatelya)
        print(text_admin)
        profiles.commit()
        await msg.answer("Фамилия пользователя изменена", reply_markup=kb.button_nazad_admin1)

    @router.callback_query(F.data == "admin_edit_name2")
    async def edit2(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите новое имя пользователя:")
        await state.set_state(ClasS.a8)

    @router.message(ClasS.a8, F.text)
    async def vvod_edit2(msg: Message):
        text_admin = msg.text
        cursor1.execute('UPDATE Users SET name2 = ? WHERE id_tg = ?', (str(text_admin), int(id_polzovatelya)))
        await msg.answer("Имя пользователя изменено", reply_markup=kb.button_nazad_admin1)
    @router.callback_query(F.data == "admin_edit_name3")
    async def edit3(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите новое отчество пользователя:")
        await state.set_state(ClasS.a9)

    @router.message(ClasS.a9, F.text)
    async def vvod_edit3(msg: Message):
        text_admin = msg.text
        cursor1.execute('UPDATE Users SET name3 = ? WHERE id_tg = ?', (str(text_admin), int(id_polzovatelya)))
        await msg.answer("Отчество пользователя изменено", reply_markup=kb.button_nazad_admin1)

    @router.callback_query(F.data == "admin_edit_otdel")
    async def edit4(msg: Message, state: FSMContext):
        await msg.message.answer("Введите новый отдел пользователя:")
        await state.set_state(ClasS.a10)

    @router.message(ClasS.a10, F.text)
    async def vvod_edit4(msg: Message):
        text_admin = msg.text
        cursor1.execute('UPDATE Users SET otdel = ? WHERE id_tg = ?', (str(text_admin), int(id_polzovatelya)))
        await msg.answer("Отдел пользователя изменено", reply_markup=kb.button_nazad_admin1)


    @router.callback_query(F.data == "admin_edit_admin")
    async def edit5(msg: types.CallbackQuery):
        cursor1.execute('UPDATE Users SET admin = ? WHERE id_tg = ?', (int(1), int(id_polzovatelya)))
        await msg.message.answer("Статус пользователя изменен", reply_markup=kb.button_nazad_admin1)

    @router.callback_query(F.data == "admin_edit_bal")
    async def edit6(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите новый баланс пользователя:")
        await state.set_state(ClasS.a11)

    @router.message(ClasS.a11, F.text)
    async def vvod_edit6(msg: Message):
        text_admin = ord(msg.text)
        cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (int(text_admin), int(id_polzovatelya)))
        await msg.answer("Баланс пользователя изменен", reply_markup=kb.button_nazad_admin1)



    @router.callback_query(F.data == "zakaz_user_view")
    async def zakaz_edit(msg: types.CallbackQuery):
        await msg.message.answer("Выберите заказ:")
        cursor3.execute('SELECT * FROM Zakaz_base')
        zakazi = cursor3.fetchall()

        for zakaz in zakazi:
            await msg.message.answer(f"ID: {zakaz[0]}\nID получателя: {zakaz[1]}\n",
                                     reply_markup=kb.button_vibor_admin2)
            global id_zakaz
            id_zakaz = zakaz[0]
            await msg.message.answer("", reply_markup=kb.menu_balance)

    @router.callback_query(F.data == "vibor2_admin")
    async def vibor_zakaza_admin(msg: types.CallbackQuery):
        cursor3.execute('SELECT * FROM Zakaz_base WHERE id=?', (int(id_zakaz),))
        row = cursor3.fetchall()
        for zakaz in row:
            await msg.message.answer(
                        f"ID: {zakaz[0]}\nID получателя: {zakaz[1]}\nЦена: {zakaz[2]}\nПункт получения: {zakaz[3]}\nСтатус: {zakaz[4]}\nСрок хранения: {zakaz[5]}\nБыл ли заказ продлен: {zakaz[6]}\n",
                        reply_markup=kb.menu_admin3)

    @router.callback_query(F.data == "admin_edit_punkt")
    async def edit1_1(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите пункт выдачи:")
        await state.set_state(ClasS.a12)
    @router.message(ClasS.a12, F.text)
    async def vvod_edit1_1(msg: Message):
        text_admin = msg.text
        cursor3.execute('UPDATE Zakaz_base SET punkt = ? WHERE id = ?', (str(text_admin), int(id_zakaz)))
        await msg.answer("Пункт выдачи изменен", reply_markup=kb.button_nazad_admin2)

    @router.callback_query(F.data == "admin_edit_status")
    async def edit1_2(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите статус заказа:")
        await state.set_state(ClasS.a13)

    @router.message(ClasS.a13, F.text)
    async def vvod_edit1_2(msg: Message):
        text_admin = msg.text
        cursor3.execute('UPDATE Zakaz_base SET status = ? WHERE id = ?', (str(text_admin), int(id_zakaz)))
        await msg.answer("Статус заказа изменен", reply_markup=kb.button_nazad_admin2)

    @router.callback_query(F.data == "admin_edit_srok")
    async def edit1_3(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите срок хранения:")
        await state.set_state(ClasS.a14)

    @router.message(ClasS.a14, F.text)
    async def vvod_edit1_3(msg: Message):
        text_admin = msg.text
        cursor3.execute('UPDATE Zakaz_base SET srok = ? WHERE id = ?', (str(text_admin), int(id_zakaz)))
        await msg.answer("Срок хранения изменен", reply_markup=kb.button_nazad_admin2)

    @router.callback_query(F.data == "shop_tovari_view")
    async def tovar_edit(msg: types.CallbackQuery):
        await msg.message.answer("Выберите товар:")
        cursor2.execute('SELECT * FROM Shop_base')
        tovari = cursor2.fetchall()

        for tovar in tovari:
            await msg.message.answer(f"ID: {tovar[0]}\nНазвание: {tovar[1]}\n",
                                     reply_markup=kb.button_vibor_admin3)
            global id_tov
            id_tov = tovar[0]
            await msg.message.answer("", reply_markup=kb.add_tovar)

    @router.callback_query(F.data == "vibor3_admin")
    async def vibor_tovara_admin(msg: types.CallbackQuery):
        cursor2.execute('SELECT * FROM Shop_base WHERE id=?', (int(id_tov), ))
        row = cursor2.fetchall()
        file_ids = []
        with open("1.png", "rb") as image_from_buffer:
            result = await msg.message.answer_photo(BufferedInputFile(image_from_buffer.read(), filename="image from buffer.jpg"), caption="Изображение из буфера")
            file_ids.append(result.photo[-1].file_id)
        await msg.message.answer("Отправленные файлы:\n" + "\n".join(file_ids))
        for tovar in row:

            await msg.message.answer(
                f"ID: {tovar[0]}\nНазвание товара: {tovar[1]}\nЦена товара: {tovar[2]}\n",
                            reply_markup=kb.menu_admin4)

    @router.callback_query(F.data == "admin_edit_namet")
    async def edit2_1(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите наименование товара:")
        await state.set_state(ClasS.a15)

    @router.message(ClasS.a15, F.text)
    async def vvod_edit2_1(msg: Message):
        text_admin = msg.text
        cursor2.execute('UPDATE Shop_base SET name = ? WHERE id = ?', (str(text_admin), int(id_tov)))
        await msg.answer("Название товара изменено", reply_markup=kb.button_nazad_admin3)

    @router.callback_query(F.data == "admin_edit_price")
    async def edit2_2(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите цену товара:")
        await state.set_state(ClasS.a16)

    @router.message(ClasS.a16, F.text)
    async def vvod_edit2_2(msg: Message):
        text_admin = msg.text
        cursor2.execute('UPDATE Shop_base SET price = ? WHERE id = ?', (int(text_admin), int(id_tov)))
        await msg.answer("Цена товара изменена", reply_markup=kb.button_nazad_admin3)

    @router.callback_query(F.data == "admin_edit_image")
    async def edit2_3(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Пришлите изображение товара:")
        await state.set_state(ClasS.a17)

    @router.message(ClasS.a17,)
    async def vvod_edit2_3(msg: Message):
        image_admin = msg.document
        await bot.download_file("img/", "1.png")
        emp_photo = convert_to_binary_data('img/am.jpg')
        cursor2.execute('UPDATE Shop_base SET image = ? WHERE id = ?', (emp_photo, int(id_tov)))
        await msg.answer("Изображение товара изменено", reply_markup=kb.button_nazad_admin3)

    @router.callback_query(F.data == "add_tovar")
    async def add_tovar(msg: types.CallbackQuery, state: FSMContext):
        await msg.message.answer("Введите название товара")
        await state.set_state(Tovar1.name)

    @router.message(Tovar1.name, F.text)
    async def add_tovar1(msg: Message, state: FSMContext):
        Tovar.name = msg.text
        await msg.answer("Введите цену товара")
        await state.set_state(Tovar1.price)

    @router.message(Tovar1.price, F.text)
    async def add_tovar2(msg: Message, state: FSMContext):
        Tovar.price = ord(msg.text)
        await msg.answer("Отправьте изображаение товара")
        await state.set_state(Tovar1.image)

    @router.message(Tovar1.image, F.text)
    async def add_tovar3(msg: Message, state: FSMContext):
        await msg.photo[-1].download('img/am.jpg')
        Tovar.image = open('img/am.jpg', 'rb')
        emp_photo = convert_to_binary_data('img/am.jpg')
        cursor2.execute('INSERT INTO Shop_base VALUES(?, ?, ?)', (str(Tovar.name), int(Tovar.price), Tovar.image))
        await msg.answer("Товар добавлен!", reply_markup=kb.menu_balance)