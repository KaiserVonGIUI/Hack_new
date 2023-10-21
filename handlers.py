from aiogram import F, Router, Dispatcher, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from aiogram.types import Message, InputFile
from aiogram.enums.parse_mode import ParseMode


import config
import kb
import text
import sqlite3

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

korzina = []
id_tov = -1
itog_price = 0
id_zakaz = -1
id_polzovatelya = -1
fl1 = 1
fl2 = 1
flag_prodlenia = False
afl1 = 1

def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


profiles = sqlite3.connect('profiles.db')
cursor1 = profiles.cursor()

cursor1.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
id_tg INTEGER NOT NULL,
name1 TEXT NOT NULL,
name2 TEXT NOT NULL,
name3 TEXT NOT NULL,
otdel TEXT NOT NULL,
admin BLOB NOT NULL,
balance INTEGER NOT NULL)''')


profiles.commit()

shop_base = sqlite3.connect('shop_base.db')
cursor2 = shop_base.cursor()

cursor2.execute("""CREATE TABLE IF NOT EXISTS Shop_base ( id INTEGER PRIMARY KEY not null, name TEXT NOT NULL, price INTEGER NOT NULL, picture BLOB NOT NULL)""")

shop_base.commit()


zakaz_base = sqlite3.connect('zakaz_base.db')
cursor3 = zakaz_base.cursor()

cursor3.execute('''
CREATE TABLE IF NOT EXISTS Zakaz_base (
id INTEGER PRIMARY KEY,
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

class Profil:
    id_tg = 0,
    name1 = "",
    name2 = "",
    name3 = "",
    otdel = "",
    admin = False,
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

info = cursor1.execute('SELECT * FROM Users WHERE id_tg=?', (Profil.id_tg))
if info.fetchone() is None:
    @router.message(Command("start"))
    async def start_handler(msg: Message, state: FSMContext):
        await msg.answer(text.greet)
        await msg.answer(text.name1)
        await state.set_state(Profile.test123)


    @router.message(Profile.test123, F.text)
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
            Profil.admin = False
        else:
            if admin_text == "test_code":
                Profil.admin = True
            else:
                await msg.answer(text.admin1)
        await state.set_state(Profile.admin)

    Profil.bal = 0
    cursor1.execute('INSERT INTO Users VALUES(1, ?, ?, ?, ?, ?, ?, ?)',
                    (str(Profil.id_tg), str(Profil.name1), str(Profil.name2), str(Profil.name3), str(Profil.otdel), str(Profil.admin), str(Profil.bal), ))


else:
    @router.message(Command("start"))
    async def start_avtorisovaniy(msg: Message):
        Profil.id_tg = msg.from_user.id
        await msg.answer(text.welcome, reply_markup=kb.menu_balance)


    cursor1.execute('SELECT * FROM Users WHERE id_tg=?', (Profil.id_tg))
    users1 = cursor1.fetchall()
    Profil.id_tg = users1[1]
    Profil.name1 = users1[2]
    Profil.name2 = users1[3]
    Profil.name3 = users1[4]
    Profil.otdel = users1[5]
    Profil.admin = users1[6]
    Profil.bal = users1[7]

    if Profil.admin == False:
        @router.callback_query(F.data == "main_menu") #оснвное меню
        async def start_polzovatel(msg: Message):
            await msg.answer(f"Добро пожаловать, {Profile.name2} {Profil.name3}! Выберите необходимое действие", reply_markup=kb.menu_profil)

        @router.callback_query(F.data == "Valute_sharing")
        async def valute_sharing(msg: Message):
            await msg.answer("Выберите получателя:")
            cursor1.execute('SELECT id, name1, name2, name3 FROM Users WHERE admin=?', (False,))
            polzovateli = cursor1.fetchall()

            for row in polzovateli:
                await msg.answer(f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\n", reply_markup=kb.button_vibor)
                id_polzovatelya = row[0]

            await msg.answer("", reply_markup=kb.menu_balance)

        @router.callback_query(F.data == "vibor")
        async def vibor_polzovatelya(msg: Message, state: FSMContext):
            cursor1.execute('SELECT name1, name2, name3 FROM Users WHERE id=?', (id_polzovatelya,))
            polzovateli = cursor1.fetchall()
            await msg.answer(f"Фамилия: {polzovateli[1]}\nИмя: {polzovateli[2]}\nОтчество: {polzovateli[3]}\n")
            await msg.answer("Введите сумму перевода")
            await state.set_state(fl1)

        @router.message(fl1, F.text)
        async def perevod_polzovatelu(msg: Message):
            summa_perevoda = ord(msg.text)
            if summa_perevoda <= Profil.bal:
                cursor1.execute('SELECT bal FROM Users WHERE id=?', (id_polzovatelya,))
                polzovatel = cursor1.fetchall()
                bal_1 = polzovatel + summa_perevoda
                cursor1.execute('UPDATE Users SET balance = ? WHERE id = ?', (polzovatel, id_polzovatelya))
                profiles.commit()
                Profil.bal = Profil.bal - summa_perevoda
                cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (Profil.bal, Profil.id_tg))
                await msg.answer("Перевод успешно выполнен!", reply_markup=kb.menu_balance)
            else:
                await msg.answer("Недостаточно средств на балансе!", kb.menu_balance)


        @router.callback_query(F.data == "zakaz_view")
        async def zakaz_view(msg: Message):
            cursor3.execute('SELECT * FROM Zakaz_base WHERE id_user=?', (Profil.id_tg,))
            zakazi = cursor3.fetchall()
            for zakaz in zakazi:
                await msg.answer(f"ID заказа: {zakaz[0]}\nСумма заказа: {zakaz[2]}\nПункт выдачи: {zakaz[3]}\nСтатус заказа: {zakaz[4]}\nСрок хранения: {zakaz[5]}\nБыл ли продлен срок хранения:: {zakaz[6]}\n", reply_markup=kb.button_vibor1)
                id_zakaz = zakaz[0]
                flag_prodlenia = zakaz[6]
            await msg.answer("", reply_markup=kb.menu_balance)

        @router.callback_query(F.data == "vibor1")
        async def zakaz_prodlit(msg: Message, state: FSMContext):
            cursor3.execute('SELECT srok, vopros FROM Zakaz_base WHERE id=?', (id_zakaz,))
            zakaz = cursor3.fetchall()
            if flag_prodlenia == False:
                await msg.answer("Введите дату крайнего срока получения заказа. Повторно продлить заказ нельзя. Если Вы не получите заказ до назначенного срока, заказ будет отменен администраторами")
                await state.set_state(fl2)
            else:
                await msg.answer("Заказ уже был продлен. Повторное продление невозможно", reply_markup=kb.menu_balance)

        @router.message(fl2, F.text)
        async def vvod_dati(msg: Message):
            date = msg.text
            cursor3.execute('UPDATE Zakaz_base SET srok = ? WHERE id = ?', (date, id_zakaz))
            zakaz_base.commit()
            await msg.answer("Срок хранения заказа успешно продлен!", reply_markup=kb.menu_balance)


        @router.callback_query(F.data == "balance") #просмотр баланса
        async def view_balance(msg: Message):
            await msg.answer(f"Ваш баланс равен: {Profil.bal}", reply_markup=kb.menu_balance)

        @router.callback_query(F.data == "shop_page")
        @router.callback_query(F.data == "iz_korzina")
        async def shop(msg: Message):
            cursor2.execute('SELECT * FROM Shop_base')
            results = cursor2.fetchall()

            for row in results:
                await msg.answer(f"Наименование: {row[1]}\nID: {row[0]}\n")
                photo = InputFile(row[3])
                await bot.send_photo(photo=photo)
                await msg.answer(f"Цена: {row[2]}\n", reply_markup=kb.button_korzina)
                id_tov = row[0]

            await msg.answer("Меню", reply_markup=kb.menu_shop1)

        @router.callback_query(F.data == "zakaz_oformlenie")
        async def korzina_oformlenie(msg: Message):
            for i in korzina:
                cursor2.execute('SELECT * FROM Shop_base WHERE id=?', (korzina[i]))
                result = cursor2.fetchall()
                await msg.answer(f"Наименование: {result[1]}\nЦена: {result[2]}")
                itog_price = itog_price + result[2]
            await msg.answer(f"Итого: {itog_price}", reply_markup=kb.menu_shop2)

        @router.callback_query(F.data == "oplata")
        async def oplata(msg: Message):
            if itog_price <= Profil.bal:
                Profil.bal = Profile.bal - itog_price
                cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (Profil.bal, Profil.id_tg))
                profiles.commit()
                cursor1.execute('SELECT id_tg FROM Users WHER admin=?', (True,))
                admins = cursor1.fetchall()
                for admin in admins:
                    await bot.send_message(admins[admin], f"Новый заказ от пользователя {Profil.id_tg}: {Profil.name1} {Profil.name2} {Profil.name3} на сумму {itog_price}")
                korzina.clear()
                await msg.answer("Оплата успешна!\nОтслеживать статус заказа вы можете в соответствующем разделе!", reply_markup=kb.menu_balance)
            else:
                await msg.answer("Недостаточно средств на балансе!", reply_markup=kb.menu_shop3)


        @router.callback_query(F.data == "otmena")
        async def otmena_zakaz(msg: Message):
            korzina.clear()
            await msg.answer("Заказ отменен!", reply_markup=kb.menu_balance)


            


        @router.callback_query(F.data == "in_korzina")
        async def in_korzina(msg: Message):
            korzina.append(id_tov)
            await msg.answer(text.in_korzina, reply_markup=kb.button_back_korzina)



        @router.callback_query(F.data == "profile_view") #просмотр профиля
        async def profile_view(msg: Message):
            await msg.answer(f"Фамилия: {Profil.name1}\nИмя: {Profil.name2}\nОтчество: {Profil.name3}\nОтдел: {Profil.otdel}\nАдминистратор: нет", reply_markup=kb.menu_profil1)

        @router.callback_query(F.data == "profile_edit") #редактирование профиля
        async def edit_profile(msg: Message, state: FSMContext):
            await msg.answer(text.name1)
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
                Profil.admin = False
            else:
                if admin_text == "test_code":
                    Profil.admin = True
                else:
                    await msg.answer(text.admin1)
            await state.set_state(Profile.admin)
            cursor1.execute('UPDATE Users SET name1 = ? WHERE id_tg = ?', (Profil.name1, Profil.id_tg))
            cursor1.execute('UPDATE Users SET name2 = ? WHERE id_tg = ?', (Profil.name2, Profil.id_tg))
            cursor1.execute('UPDATE Users SET name3 = ? WHERE id_tg = ?', (Profil.name3, Profil.id_tg))
            cursor1.execute('UPDATE Users SET otdel = ? WHERE id_tg = ?', (Profil.otdel, Profil.id_tg))
            cursor1.execute('UPDATE Users SET admin = ? WHERE id_tg = ?', (Profil.admin, Profil.id_tg))
            cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (Profil.balance, Profil.id_tg))
            profiles.commit()
    else:
        @router.callback_query(F.data == "main_menu") #оснвное меню
        async def start_admin(msg: Message):
            await msg.answer(f"Добро пожаловать, администратор {Profile.name2} {Profil.name3}! Выберите необходимое действие", reply_markup=kb.menu_admin)

        @router.callback_query(F.data == "profile_user_view")
        async def user_profile_edit(msg: Message):
            await msg.answer("Выберите пользователя:")
            cursor1.execute('SELECT * FROM Users WHERE admin=?', (False,))
            polzovateli = cursor1.fetchall()

            for row in polzovateli:
                await msg.answer(f"Фамилия: {row[1]}\nИмя: {row[2]}\nОтчество: {row[3]}\n", reply_markup=kb.button_vibor_admin1)
                id_polzovatelya = row[0]
                await msg.answer("", reply_markup=kb.menu_balance)

            @router.callback_query(F.data == "vibor1_admin")
            async def vibor_polzovatelya_admin(msg: Message):
                cursor1.execute('SELECT * FROM Users WHERE id=?', (id_polzovatelya,))
                polzovatel = cursor1.fetchall()
                await msg.answer(f"ID: {polzovatel[0]}\nФамилия: {polzovatel[1]}\nИмя: {polzovatel[2]}\nОтчество: {polzovatel[3]}\nОтдел: {polzovatel[4]}\nАдминистратор: нет\nБаланс: {polzovatel[6]}",reply_markup=kb.menu_admin2)

            @router.callback_query(F.data == "admin_edit_name1")
            async def edit1(msg: Message, state: FSMContext):
                await msg.answer("Введите новую фамилию пользователя:")
                await state.set_state(afl1)

            @router.message(afl1, F.text)
            async def vvod_edit1(msg: Message):
                text_admin = msg.text
                cursor1.execute('UPDATE Users SET name1 = ? WHERE id_tg = ?', (text_admin, id_polzovatelya))
                await msg.answer("Фамилия пользователя изменена", reply_markup=kb.button_nazad_admin1)

            @router.callback_query(F.data == "admin_edit_name2")
            async def edit2(msg: Message, state: FSMContext):
                await msg.answer("Введите новое имя пользователя:")
                await state.set_state(afl1)

            @router.message(afl1, F.text)
            async def vvod_edit2(msg: Message):
                text_admin = msg.text
                cursor1.execute('UPDATE Users SET name2 = ? WHERE id_tg = ?', (text_admin, id_polzovatelya))
                await msg.answer("Имя пользователя изменено", reply_markup=kb.button_nazad_admin1)

            @router.callback_query(F.data == "admin_edit_name3")
            async def edit3(msg: Message, state: FSMContext):
                await msg.answer("Введите новое отчество пользователя:")
                await state.set_state(afl1)

            @router.message(afl1, F.text)
            async def vvod_edit3(msg: Message):
                text_admin = msg.text
                cursor1.execute('UPDATE Users SET name3 = ? WHERE id_tg = ?', (text_admin, id_polzovatelya))
                await msg.answer("Отчество пользователя изменено", reply_markup=kb.button_nazad_admin1)

            @router.callback_query(F.data == "admin_edit_otdel")
            async def edit4(msg: Message, state: FSMContext):
                await msg.answer("Введите новый отдел пользователя:")
                await state.set_state(afl1)

            @router.message(afl1, F.text)
            async def vvod_edit4(msg: Message):
                text_admin = msg.text
                cursor1.execute('UPDATE Users SET otdel = ? WHERE id_tg = ?', (text_admin, id_polzovatelya))
                await msg.answer("Отдел пользователя изменено", reply_markup=kb.button_nazad_admin1)


            @router.callback_query(F.data == "admin_edit_admin")
            async def edit5(msg: Message):
                cursor1.execute('UPDATE Users SET admin = ? WHERE id_tg = ?', (True, id_polzovatelya))
                await msg.answer("Статус пользователя изменен", reply_markup=kb.button_nazad_admin1)

            @router.callback_query(F.data == "admin_edit_bal")
            async def edit6(msg: Message, state: FSMContext):
                await msg.answer("Введите новый баланс пользователя:")
                await state.set_state(afl1)

            @router.message(afl1, F.text)
            async def vvod_edit6(msg: Message):
                text_admin = ord(msg.text)
                cursor1.execute('UPDATE Users SET balance = ? WHERE id_tg = ?', (text_admin, id_polzovatelya))
                await msg.answer("Баланс пользователя изменен", reply_markup=kb.button_nazad_admin1)



            @router.callback_query(F.data == "zakaz_user_view")
            async def zakaz_edit(msg: Message):
                await msg.answer("Выберите заказ:")
                cursor3.execute('SELECT * FROM Zakaz_base')
                zakazi = cursor3.fetchall()

                for zakaz in zakazi:
                    await msg.answer(f"ID: {zakaz[0]}\nID получателя: {zakaz[1]}\n",
                                     reply_markup=kb.button_vibor_admin2)
                    id_zakaz = zakaz[0]
                    await msg.answer("", reply_markup=kb.menu_balance)

                @router.callback_query(F.data == "vibor2_admin")
                async def vibor_zakaza_admin(msg: Message):
                    cursor3.execute('SELECT * FROM Zakaz_base WHERE id=?', (id_zakaz,))
                    zakaz = cursor3.fetchall()
                    await msg.answer(
                        f"ID: {zakaz[0]}\nID получателя: {zakaz[1]}\nЦена: {zakaz[2]}\nПункт получения: {zakaz[3]}\nСтатус: {zakaz[4]}\nСрок хранения: {zakaz[5]}\nБыл ли заказ продлен: {zakaz[6]}\n",
                        reply_markup=kb.menu_admin3)

                @router.callback_query(F.data == "admin_edit_punkt")
                async def edit1_1(msg: Message, state: FSMContext):
                    await msg.answer("Введите пункт выдачи:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit1_1(msg: Message):
                    text_admin = msg.text
                    cursor3.execute('UPDATE Zakaz_base SET punkt = ? WHERE id = ?', (text_admin, id_zakaz))
                    await msg.answer("Пункт выдачи изменен", reply_markup=kb.button_nazad_admin2)

                @router.callback_query(F.data == "admin_edit_status")
                async def edit1_2(msg: Message, state: FSMContext):
                    await msg.answer("Введите статус заказа:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit1_2(msg: Message):
                    text_admin = msg.text
                    cursor3.execute('UPDATE Zakaz_base SET status = ? WHERE id = ?', (text_admin, id_zakaz))
                    await msg.answer("Статус заказа изменен", reply_markup=kb.button_nazad_admin2)

                @router.callback_query(F.data == "admin_edit_srok")
                async def edit1_3(msg: Message, state: FSMContext):
                    await msg.answer("Введите срок хранения:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit1_3(msg: Message):
                    text_admin = msg.text
                    cursor3.execute('UPDATE Zakaz_base SET srok = ? WHERE id = ?', (text_admin, id_zakaz))
                    await msg.answer("Срок хранения изменен", reply_markup=kb.button_nazad_admin2)

                @router.callback_query(F.data == "shop_tovari_view")
                async def tovar_edit(msg: Message):
                    await msg.answer("Выберите товар:")
                    cursor2.execute('SELECT * FROM Shop_base')
                    tovari = cursor2.fetchall()

                    for tovar in tovari:
                        await msg.answer(f"ID: {tovar[0]}\nНазвание: {tovar[1]}\n",
                                         reply_markup=kb.button_vibor_admin3)
                        id_tov = tovar[0]
                        await msg.answer("", reply_markup=kb.add_tovar)

                @router.callback_query(F.data == "vibor3_admin")
                async def vibor_tovara_admin(msg: Message):
                    cursor2.execute('SELECT * FROM Shop_base WHERE id=?', (id_tov,))
                    tovar = cursor2.fetchall()
                    await bot.send_photo(tovar[3])
                    await msg.answer(
                        f"ID: {tovar[0]}\nНазвание товара: {tovar[1]}\nЦена товара: {tovar[2]}\n",
                        reply_markup=kb.menu_admin4)

                @router.callback_query(F.data == "admin_edit_namet")
                async def edit2_1(msg: Message, state: FSMContext):
                    await msg.answer("Введите наименование товара:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit2_1(msg: Message):
                    text_admin = msg.text
                    cursor2.execute('UPDATE Shop_base SET name = ? WHERE id = ?', (text_admin, id_tov))
                    await msg.answer("Название товара изменено", reply_markup=kb.button_nazad_admin3)

                @router.callback_query(F.data == "admin_edit_price")
                async def edit2_2(msg: Message, state: FSMContext):
                    await msg.answer("Введите цену товара:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit2_2(msg: Message):
                    text_admin = msg.text
                    cursor2.execute('UPDATE Shop_base SET price = ? WHERE id = ?', (text_admin, id_tov))
                    await msg.answer("Цена товара изменена", reply_markup=kb.button_nazad_admin3)

                @router.callback_query(F.data == "admin_edit_image")
                async def edit2_3(msg: Message, state: FSMContext):
                    await msg.answer("Пришлите изображение товара:")
                    await state.set_state(afl1)

                @router.message(afl1, F.text)
                async def vvod_edit2_3(msg: Message):
                    await msg.photo[-1].download('img/am.jpg')
                    image_admin = open('img/am.jpg', 'rb')
                    emp_photo = convert_to_binary_data('img/am.jpg')
                    cursor2.execute('UPDATE Shop_base SET image = ? WHERE id = ?', (emp_photo, id_tov))
                    await msg.answer("Изображение товара изменено", reply_markup=kb.button_nazad_admin3)

                @router.callback_query(F.data == "add_tovar")
                async def add_tovar(msg: Message, state: FSMContext):
                    await  msg.answer("Введите название товара")
                    await state.set_state(Tovar1.name)

                @router.message(Tovar1.name, F.text)
                async def add_tovar1(msg: Message, state: FSMContext):
                    Tovar.name = msg.text
                    await  msg.answer("Введите цену товара")
                    await state.set_state(Tovar1.price)

                @router.message(Tovar1.price, F.text)
                async def add_tovar2(msg: Message, state: FSMContext):
                    Tovar.price = ord(msg.text)
                    await  msg.answer("Отправьте изображаение товара")
                    await state.set_state(Tovar1.image)

                @router.message(Tovar1.image, F.text)
                async def add_tovar3(msg: Message, state: FSMContext):
                    await msg.photo[-1].download('img/am.jpg')
                    Tovar.image = open('img/am.jpg', 'rb')
                    emp_photo = convert_to_binary_data('img/am.jpg')
                    cursor2.execute('INSERT INTO Shop_base VALUES(?, ?, ?)', (Tovar.name, Tovar.price, Tovar.image))
                    await msg.answer("Товар добавлен!", reply_markup=kb.menu_balance)