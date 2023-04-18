import telebot
from telebot import types
bot = telebot.TeleBot('5867712863:AAETiVY68RBg2-gzIXVoHrKujS1Yz8ceZfI')

# states = ['start', 'show note', 'choose item', 'displaying note', 'create note', 'enter item number',
#           'enter item name', 'enter note body', 'delete note']

db = [{'Номер': '1', 'Название': 'denis', 'Тело заметки': 'dobrynin'},
      {'Номер': '2', 'Название': 'aza', 'Тело заметки': 'kara'}]
temp_db = []

# current_state = states[0]
# new_note_point = 0
# new_note_name = None
# new_note_body = None


def main():
    while True:
        show_main_menu()


@bot.message_handler(commands=['start'])
def show_main_menu(message):
    bot.send_message(message.chat.id, "Выбери, чем хочешь заняться:\n\nПосмотреть меню 'show notes'"
                                      "\nНайти заметки 'find note'\nСоздать заметку 'create note'"
                                      "\nУдалить заметку 'delete note'")
@bot.message_handler(commands=['button'])


    if input_command == "find note":
        finding_notes()

    elif input_command == "create note":
        creating_note()

    elif input_command == "show notes":
        titles()

    elif input_command == "delete note":
        deleting_note()

    else:
        show_main_menu()


def titles():
    if len(db) == 0:
        print("Заметки отсутсвуют")
        show_main_menu()
    else:
        for d in db:
            print(f"{d['Номер']} {d['Название']}")
    print(db)
    print("\nДля выхода в главное меню напишите start")
    user_command = input()

    if user_command == "start":
        show_main_menu()
    else:
        print("Некорректный ввод")
        show_main_menu()


def finding_notes():
    print("Выбери номер или название")
    user_input = input()
    for dicts in db:

        if dicts['Номер'] == user_input or dicts["Название"] == user_input:
            print("По вашему запросу найдена заметка.\nЧтобы продолжить поиск введите search\n"
                  "Чтобы перейти к найденой заметке нажмите go\nЧтобы вернуться в главное меню нажмите "
                  "start")
            user_command = input()

            if user_command == "go":
                print(f"{dicts['Номер']} {dicts['Название']}\n{dicts['Тело заметки']}")
                finding_other_note_or_start()

            if user_command == "search":
                continue

            elif user_command == "start":
                show_main_menu()
    else:
        print("Заметка не найдена")
        print("\nЧтобы выбрать другую заметку нажмите back\n"
              "Чтобы вернуться в главное меню нажмите start")
        user_command = input()

        if user_command == "back":
            finding_notes()
        elif user_command == "start":
            show_main_menu()


def finding_other_note_or_start():
    print("\nЧтобы выбрать другую заметку нажмите back\n"
          "Чтобы вернуться в главное меню нажмите start")
    user_command = input()

    if user_command == "back":
        finding_notes()
    elif user_command == "start":
        show_main_menu()


def creating_note():
    dct = dict()

    number = input_note_number()
    num = check_on_integer(number)

    if check_for_matches(str(num)) is True:
        print("Такой номер уже существуют, введите другой, "
              "либо удалите существующую заметку")
        creating_note()
    else:
        print("Номер сохранен")

    title = input_note_title()
    body = input_note_body()
    dct["Номер"] = num
    dct["Название"] = title
    dct["Тело заметки"] = body

    db.append(dct)
    print("Заметка добавлена\n")
    show_main_menu()


def check_for_matches(arg):
    flag = False
    for d in db:
        if arg in d.values():
            flag = True

    return flag


def check_on_integer(number):
    lst = list(str(number))
    ind = lst.index('.')
    mark = True

    for i in lst[ind + 1:]:
        if i != '0':
            mark = False
            break

    if mark is True:
        return int(number)
    else:
        return number


def input_note_number():
    print("Введи номер пункта\nЧтобы вернуться в главное меню, напиши start\n")
    num = input()

    if num == "start":
        show_main_menu()
    else:
        try:
            float(num)
        except ValueError:
            print("Некорректно набран номер")
            input_note_number()

    return float(num)


def input_note_title():
    print("Введи название заметки\nЧтобы вернуться в главное меню, напиши start\n"
          "Чтобы заново ввести номер пункта меню напиши note number")
    title = input()

    if title == "start":
        show_main_menu()
    elif title == "note number":
        input_note_number()
        input_note_title()
    else:
        flag = check_for_matches(title)

        if flag is True:
            print("Такое название уже существует, напишите другое название, или удалите существующее")
            creating_note()
        else:
            print("Название сохранено")
            return title


def input_note_body():
    print("Введи заметку\nЧтобы вернуться в главное меню, напиши start\n"
          "Чтобы заново ввести название заметки напиши note title")
    body = input()
    if body == "start":
        show_main_menu()
    elif body == "note title":
        input_note_title()
        input_note_body()
    else:
        return body


def deleting_note():
    print("Выберете номер или название удаляемой заметки")
    user_input = input()
    marker = False

    for d in db:

        if d["Номер"] == user_input or d["Название"] == user_input:
            d.clear()
            marker = True
            break
    else:
        print('Заметки не найдено\n')

    if marker is True:
        deleting_empty_dict()
        print('Заметка удалена\n')

    print("Чтобы удалить другую заметку напишите delete\n"
          "Чтобы выйти в главное меню нажмите start")
    user_command = input()

    if user_command == "delete":
        deleting_note()
    if user_command == "start":
        show_main_menu()


def deleting_empty_dict():
    for dct in db:

        if len(dct) == 0:
            continue
        else:
            temp_db.append(dct)
    save_db()


def save_db():
    global db
    db = temp_db


bot.infinity_polling()
main()





# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = "Привет! Выбери, чем хочешь заняться:\n\nДля просмотра заметок нажми команду /show\n\n" \
#            "Для создания заметки нажми команду /create"
#     users_id = message.chat.id
#     bot.send_message(message.chat.id, mess)
#
#
# @bot.message_handler(commands=['show'])
# def show(message):
#     pass
#
#
# @bot.message_handler(commands=['create'])
# def create(message):
#     db = [dict()]
#     instruction = "Введите 'Пункт', 'Тему' или 'Заметку'"
    # Делаю структуру по типу {Пункт: 1, Тема: Питон, Заметка: Питон - это интерпретируемый язык программирования}
    # text = bot.send_message(message.chat.id, instruction)
    # print(text)
    # text2 = bot.register_next_step_handler(text, get_input_from_user)
    # print(text2)
    # get_input = get_input_from_user(message)
    # total_of_check = check_for_matches(db, get_input)
    # bot.send_message(message.chat.id, total_of_check)

    # bot.send_message(message.chat.id, instruction)
    # #dct[get_input] = get_input_from_user()
    # get_input = get_input_from_user()
    # total_of_check = check_for_matches(db, get_input)
    # bot.send_message(message.chat.id, total_of_check)


# @bot.message_handler(content_types=['text'])
# def get_input_from_user(message):
#     # warning = 'Номер заметки или текст уже существуют'
#     get_input = None
#     while get_input is None:
#         print(message.text)
#         get_input = message.text
#
#     return get_input


# def check_for_matches(db, get_input):
#     if get_input in db:
#         return "Такое значение уже существует"
#     else:
#         return "Информация добавлена"

#bot.polling(none_stop=True)

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Вау, вот это у тебя крутое фото!')
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="http://google.com"))
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Веб сайт')
#     start = types.KeyboardButton("Start")
#
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)




