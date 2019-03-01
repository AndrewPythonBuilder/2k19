import logging
import constants, base_w
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import datetime

now = datetime.datetime.now()

text = ''
photo = ''
ans = ''
part = ''
otvet = ''
answeri = var = answeris = sal = raztel = q = texts = answeri1 = q1 = raz_ph = next_ = rzdl = ss = only_text1 = only_text = only_text_op1 = only_text_op = your_self = False

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher


def start(bot, update):
    message = update.message
    global part, raztel, text, photo, answeri, var, ans, answeris, sal, q, texts, answeri1, q1, raz_ph, next_, rzdl, otvet, ss, only_text1, only_text, only_text_op, only_text_op1, your_self
    otvet = ''
    answeri = var = answeris = sal = raztel = q = texts = answeri1 = q1 = raz_ph = next_ = rzdl = ss = only_text1 = only_text = only_text_op1 = only_text_op = your_self = False
    if message.chat.id in constants.admins:
        bottons = [['Скидка'], ['Рассылка']]
        reply_markup = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=reply_markup)
    else:
        if message.chat.id in base_w.users():

            # bot.send_photo(message.chat.id, photo = photo)
            bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
            if base_w.set_razdel() != None:
                bottons.append(['Получить скидку'])
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Приветствие', reply_markup=keyboard)

        else:
            base_w.init(message.chat.id, message.chat.username)
            # bot.send_photo(message.chat.id, photo = photo)
            bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
            if base_w.set_razdel() != None:
                bottons.append(['Получить скидку'])
            keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
            bot.send_message(message.chat.id, 'Приветствие', reply_markup=keyboard)  #
    print(message.chat.id)


def answer_questions(bot, update):
    message = update.message
    global part, raztel, text, photo, answeri, var, ans, answeris, sal, q, texts, answeri1, q1, raz_ph, next_, rzdl, otvet, ss, only_text1, only_text, only_text_op, only_text_op1, your_self
    if (message.contact != None) and (otvet == ''):
        contact = update.effective_message.contact
        phone = contact.phone_number
        base_w.update(message.chat.id, phone)
        # bot.send_photo(message.chat.id, photo = photo)
        bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
        if base_w.set_razdel() != None:
            bottons.append(['Получить скидку'])
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Спасибо, ваш контакт отправлен, оператор в ближайшее время спишется с вами',
                         reply_markup=keyboard)
        for i in constants.admins:
            try:
                bot.send_message(i, 'Имя: ' + str(message.chat.username) + '\nНомер телефона: ' + str(
                    base_w.select_number(message.chat.id)) + '\nОтвет: ' + str(ans))
            except:
                pass
    elif message.text == 'Отмена' and (message.chat.id in constants.admins):
        message.text = '/start'
        start(bot, update)
    elif your_self == True:
        your_self = False
        l = base_w.set_razdel()
        te = l[-2].split('^^^^')
        otvet += message.text + '^^^^'
        I = len(otvet.split('^^^^'))-1
        if I >= len(te):
            con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
            custom_keyboard = [[con_keyboard]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            bot.sendMessage(message.chat_id, text="Для окончания опроса нужен ваш номер телефона",
                            reply_markup=reply_markup)
        else:
            re = ''
            te.append('####@LOVEISMYLOVE@')
            try:
                while ('####' not in te[I]):
                    re += te[I] + '\n'
                    I += 1
                bot.send_message(message.chat.id, text=re)
            except:
                pass
            u = te[I].split('####')
            if u[-1] != '@LOVEISMYLOVE@':
                if u[0] != 'NOOO':
                    photo = u[0]
                    re = u[1]
                    answers = u[-1].split('$')
                    bottons = []
                    for i in range(len(answers)):
                        botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                        bottons.append(botton)
                    reply_markup = InlineKeyboardMarkup(bottons)
                    bot.send_photo(message.chat.id, photo=photo, caption=re, reply_markup=reply_markup)
                else:
                    re = u[1]
                    answers = u[-1].split('$')
                    bottons = []
                    for i in range(len(answers)):
                        botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                        bottons.append(botton)
                    reply_markup = InlineKeyboardMarkup(bottons)
                    bot.send_message(message.chat.id, text=re, reply_markup=reply_markup)
            else:
                con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
                custom_keyboard = [[con_keyboard]]
                reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
                bot.sendMessage(message.chat_id, text="Для окончания опроса нужен ваш номер телефона",
                                reply_markup=reply_markup)
    elif (message.contact != None) and (otvet != ''):
        contact = update.effective_message.contact
        phone = contact.phone_number
        base_w.update(message.chat.id, phone)
        # bot.send_photo(message.chat.id, photo = photo)
        bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
        if base_w.set_razdel() != None:
            bottons.append(['Получить скидку'])
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Спасибо, ваш контакт отправлен, оператор в ближайшее время спишется с вами',
                         reply_markup=keyboard)
        ot = otvet.split('^^^^')
        l = base_w.set_razdel()
        te = l[-2].split('^^^^')
        txt = ''
        vopros = []
        for i in te:
            if "####" in i:
                vopros.append(i.split('####')[1])
        for i in range(len(ot) - 1):
            txt += '''Вопрос: %s \nОтвет: %s \n''' % (vopros[i], ot[i])
        for i in constants.admins:
            try:
                bot.send_message(i, 'Имя: ' + str(message.chat.username) + '\nНомер телефона: +' + str(
                    base_w.select_number(message.chat.id)[0]) + '\n' + str(txt) + '\nВремя заполнения: ' + str(
                    now.strftime("%d-%m-%Y %H:%M")))  # ТААААААК ЕС ЧО ТЕСТИТЬ И ИСПРАВИТЬ!
            except:
                pass
        otvet = ''
    elif message.text == 'Рассылка' and (message.chat.id in constants.admins):
        bottons = [['Текст с картинкой'], ['Опрос (рассылка c фото)'], ['Опрос (Текст)'], ['Отмена']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите:', reply_markup=keyboard)
    elif message.text == 'Опрос (Текст)' and (message.chat.id in constants.admins):
        only_text_op = True
        bot.send_message(message.chat.id, 'Напишите текст рассылки')
    elif only_text_op == True:
        only_text_op = False
        text = message.text
        bot.send_message(message.chat.id, 'Все ответы через $')
        only_text_op1 = True
    elif only_text_op1 == True:
        only_text_op1 = False
        answers = message.text.split('$')
        bottons = []
        for i in range(len(answers)):
            botton = [InlineKeyboardButton(answers[i], callback_data=answers[i])]
            bottons.append(botton)
        reply_markup = InlineKeyboardMarkup(bottons)
        words = base_w.users()
        keyboard = ReplyKeyboardMarkup([['Свой вариант']], resize_keyboard=True)
        for i in words:
            try:
                bot.send_message(i, 'Если у вас есть свой вариант, нажмите "Свой вариант" и напишите ответ',
                                 reply_markup=keyboard)
                bot.send_message(i, text=text, reply_markup=reply_markup)
            except:
                pass
        bot.send_message(message.chat.id, text=text, reply_markup=reply_markup)
    elif message.text == 'Текст с картинкой' and (message.chat.id in constants.admins):
        bot.send_message(message.chat.id, 'Пришлите фотографию с текстом в описании')
        answeri = True
    elif answeri == True and message.photo != []:
        answeri = False
        for i in base_w.users():
            try:
                bot.send_photo(i, photo=message.photo[0].file_id, caption=message.caption)
            except:
                pass
    elif message.text == 'Опрос (рассылка c фото)' and (message.chat.id in constants.admins):
        bot.send_message(message.chat.id, 'Пришлите фотографию и текст в описании')
        q = True
    elif message.photo != [] and (message.chat.id in constants.admins) and q == True:
        q = False
        photo = message.photo[0].file_id
        text = message.caption
        bot.send_message(message.chat.id, 'Все ответы через $')
        answeris = True
    elif answeris == True and (message.chat.id in constants.admins):
        answeri = False
        answers = message.text.split('$')
        bottons = []
        for i in range(len(answers)):
            botton = [InlineKeyboardButton(answers[i], callback_data=answers[i])]
            bottons.append(botton)
        reply_markup = InlineKeyboardMarkup(bottons)
        words = base_w.users()
        keyboard = ReplyKeyboardMarkup([['Свой вариант']], resize_keyboard=True)
        for i in words:
            try:
                bot.send_message(i, 'Если у вас есть свой вариант, нажмите "Свой вариант" и напишите ответ',
                                 reply_markup=keyboard)
                bot.send_photo(i, photo, caption=text, reply_markup=reply_markup)
            except:
                pass
        bot.send_photo(message.chat.id, photo, caption=text, reply_markup=reply_markup)

    elif message.text == 'Скорочтение':
        bot.send_message(message.chat.id, ' Текст')
    elif message.text == 'Робототехника':
        bot.send_message(message.chat.id, ' Текст')
    elif message.text == 'Арифметика':
        bot.send_message(message.chat.id, ' Текст')
    elif message.text == 'Свяжитесь с нами':
        bot.send_message(message.chat.id, ' Текст')
    elif (message.text == 'Получить скидку') and (base_w.set_razdel() != None):
        bottons = [['Отмена']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Пройдите опрос', reply_markup=keyboard)
        l = base_w.set_razdel()
        te = l[-2].split('^^^^')
        I = 0
        re = ''
        try:
            while ('####' not in te[I]):
                re += te[I] + '\n'
                I += 1
        except:
            pass
        if re == '':
            re = str(l[0])
        bot.send_photo(message.chat.id, photo=l[1], caption=re)
        u = te[I].split('####')
        if u[0].replace(' ', '') != 'NOOO':
            photo = u[0].replace(' ', '')
            re = u[1]
            answers = u[-1].split('$')
            bottons = []
            for i in range(len(answers)):
                botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                bottons.append(botton)
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_photo(message.chat.id, photo=photo, caption=re, reply_markup=reply_markup)
        else:
            re = u[1]
            answers = u[-1].split('$')
            bottons = []
            for i in range(len(answers)):
                botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                bottons.append(botton)
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_message(message.chat.id, text=re, reply_markup=reply_markup)

    elif message.text == 'Скидка' and (message.chat.id in constants.admins):
        bottons = [['Создать скидку', 'Включить скидку', 'Отключить скидку'], ['Удалить скидку']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)
    elif message.text == 'Удалить скидку' and (message.chat.id in constants.admins):
        wr = base_w.all_name_of_razdel()
        bottons = []
        for i in wr:
            bottons.append([i])
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите название скидки, которую хотите удалить', reply_markup=keyboard)
        ss = True
    elif ss == True:
        ss = False
        try:
            base_w.delete_razdel(message.text)
            bot.send_message(message.chat.id, 'Скидка удалена')
            message.text = 'Отмена'
            answer_questions(bot, update)
        except:
            pass
    elif message.text == 'Отключить скидку' and (message.chat.id in constants.admins):
        base_w.off_razdel()
        bot.send_message(message.chat.id, 'Скидка отключена')
    elif message.text == 'Включить скидку' and (message.chat.id in constants.admins):
        write = base_w.all_name_of_razdel()
        bottons = []
        for i in write:
            bottons.append([i])
        bottons.append(['Отмена'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id,
                         'Выберите скидку, который вы хотите включить. \nКак только вы включите один скидку, другой, который был включен до этого, выключится',
                         reply_markup=keyboard)
        rzdl = True
    elif rzdl == True:
        rzdl = False
        if message.text == 'Отмена':
            answer_questions(bot, update)
        else:
            try:
                bot.send_message(message.chat.id,
                                 'Ваша скидка включен, теперь у пользователей появилась кнопка "Получить скидку"')
                base_w.on_razdel(message.text)
                update.message.text = 'Отмена'
                answer_questions(bot, update)
            except:
                bot.send_message(message.chat.id, 'Вы уверены, что правильно ввели название?')
                update.message.text = 'Отмена'
                answer_questions(bot, update)
    elif message.text == 'Создать скидку' and (message.chat.id in constants.admins):
        bot.send_message(message.chat.id, 'Напишите название скидки')
        next_ = True
    elif message.text == 'Отмена' and (message.chat.id in constants.admins):
        answeri = var = answeris = sal = raztel = q = texts = answeri1 = q1 = raz_ph = next_ = rzdl = ss = only_text1 = only_text = only_text_op1 = only_text_op = your_self = False
        bottons = [['Скидка'], ['Рассылка']]
        reply_markup = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=reply_markup)
    elif next_ == True:
        next_ = False
        part = message.text
        base_w.create_razdel(message.text)
        raz_ph = True
        bot.send_message(message.chat.id, 'Скиньте фотографию скидки')
    elif raz_ph == True:
        raz_ph = False
        if message.photo != []:
            bot.send_message(message.chat.id, 'Ваша фотография успешно сохранена')
            base_w.save_photo(message.photo[0].file_id, part)
            raztel = True
            answer_questions(bot, update)
        else:
            bot.send_message(message.chat.id, 'Вы уверены, что скинули фотграфию?! нажмите на /start')
    elif raztel == True:
        raztel = False
        bottons = [['Текст', 'Опрос с фото', 'Опрос (только текст)'], ['Отмена']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Выберите что будет в вашей скидке', reply_markup=keyboard)
    elif message.text == 'Опрос (только текст)':
        only_text = True
        bot.send_message(message.chat.id, 'Напишите текст опроса')
    elif only_text == True:
        only_text = False
        text = message.text
        bottons = [['Свой ответ']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Все ответы через $', reply_markup=keyboard)
        only_text1 = True
    elif only_text1 == True:
        only_text1 = False
        if message.text != 'Свой ответ':
            answers = message.text.split('$')
            bottons = []
            for i in range(len(answers)):
                botton = [InlineKeyboardButton(answers[i], callback_data='sale+' + answers[i])]
                bottons.append(botton)
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_message(message.chat.id, text=text, reply_markup=reply_markup)
            # base_save_razdel
            base_w.add_text_to_rezel('NOOO####' + str(text) + '####' + message.text + '^^^^', part)
            raztel = True
            answer_questions(bot, update)
        else:
            bottons = [[InlineKeyboardButton('Ваш ответ', callback_data='sale+Ваш ответ')]]
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_message(message.chat.id, text=text, reply_markup=reply_markup)
            base_w.add_text_to_rezel('NOOO####' + str(text) + '####' + message.text + '^^^^', part)
            raztel = True
            answer_questions(bot, update)
    elif message.text == 'Текст':
        bot.send_message(message.chat.id, 'Введите текст')
        texts = True
    elif texts == True:
        texts = False
        base_w.add_text_to_rezel(message.text + '^^^^', part)
        bot.send_message(message.chat.id, 'Ваш текст сохранен')
        raztel = True
        answer_questions(bot, update)
    elif message.text == 'Опрос с фото':
        bot.send_message(message.chat.id, 'Пришлите фотографию и текст в описании')
        q1 = True
    elif message.photo != [] and (message.chat.id in constants.admins) and q1 == True:
        q1 = False
        photo = message.photo[0].file_id
        text = message.caption
        bottons = [['Свой ответ']]
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Все ответы через $', reply_markup=keyboard)
        answeri1 = True


    elif answeri1 == True and (message.chat.id in constants.admins):
        answeri1 = False
        if message.text != 'Свой ответ':
            answers = message.text.split('$')
            bottons = []
            for i in range(len(answers)):
                botton = [InlineKeyboardButton(answers[i], callback_data='sale+' + answers[i])]
                bottons.append(botton)
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_photo(message.chat.id, photo, caption=text, reply_markup=reply_markup)
            # base_save_razdel
            base_w.add_text_to_rezel(str(photo) + '####' + str(text) + '####' + message.text + '^^^^', part)
            raztel = True
            answer_questions(bot, update)
        else:
            bottons = [[InlineKeyboardButton('Ваш ответ', callback_data='sale+Ваш ответ')]]
            reply_markup = InlineKeyboardMarkup(bottons)
            bot.send_photo(message.chat.id, photo, caption=text, reply_markup=reply_markup)
            base_w.add_text_to_rezel(str(photo)+ '####' + str(text) + '####' + message.text + '^^^^', part)
            raztel = True
            answer_questions(bot, update)

    elif message.text == 'О сервисе':
        bot.send_message(message.chat.id, 'Здесь информация о нас')

    elif message.text == 'Создать опрос' and (message.chat.id in constants.admins):
        bot.send_message(message.chat.id, 'Пришлите фотографию и текст в описании')
        q = True

    elif message.text == 'Статистика' and (message.chat.id in constants.admins):  # Сделать после перевода денег
        pass

    elif message.text == 'Свой вариант':
        var = True
        bot.send_message(message.chat.id, 'Напишите свой ответ')

    elif var == True:
        var = False
        bot.send_message(message.chat.id, 'Спасибо за ответ')
        for i in constants.admins:
            try:
                bot.send_message(i, 'Имя: ' + message.chat.username + '\nНомер телефона: +' + str(
                    base_w.select_number(message.chat.id)[0]) + '\nОтвет: ' + message.text)
            except:
                pass
    elif message.text == 'Отмена' and (message.chat.id not in constants.admins):
        # bot.send_photo(message.chat.id, photo = photo)
        bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
        if base_w.set_razdel() != None:
            bottons.append(['Получить скидку'])
        keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
        bot.send_message(message.chat.id, 'Спасибо за ваш голос', reply_markup=keyboard)
    else:
        message.text = '/start'
        start(bot, update)


def button(bot, update):
    global otvet, your_self
    try:
        query = update.callback_query
        if str(query.data).split('+')[0] == 'sale':
            global ans
            ans = str(query.data).split('+')[1]
            bot.edit_message_caption(message_id=query.message.message_id,
                                     caption="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                     chat_id=query.message.chat.id)
            con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
            custom_keyboard = [[con_keyboard]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            bot.sendMessage(query.message.chat.id, text="Для окончания опроса нужен ваш номер телефона",
                            reply_markup=reply_markup)  # НЕ работает!!!!!!!!
        else:
            try:
                I = int(str((query.data).split('+')[0])) + 1
                l = base_w.set_razdel()
                te = l[-2].split('^^^^')
                if I == len(te) and str(query.data).split('+')[1] != 'Свой ответ':
                    otvet += str(query.data).split('+')[1] + '^^^^'
                    bot.edit_message_caption(message_id=query.message.message_id,
                                             caption="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                             chat_id=query.message.chat_id)
                    con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
                    custom_keyboard = [[con_keyboard]]
                    reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
                    bot.sendMessage(query.message.chat_id, text="Для окончания опроса нужен ваш номер телефона",
                                    reply_markup=reply_markup)
                elif str(query.data).split('+')[1] == 'Свой ответ':
                    try:
                        bot.edit_message_caption(message_id=query.message.message_id,
                                                 caption="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                                 chat_id=query.message.chat_id)
                    except:
                        bot.edit_message_text(message_id=query.message.message_id,
                                              text="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                              chat_id=query.message.chat_id)
                    re = ''
                    te.append('####@LOVEISMYLOVE@')
                    try:
                        while ('####' not in te[I]):
                            re += te[I] + '\n'
                            I += 1
                        bot.send_message(query.message.chat.id, text=re)
                    except:
                        pass

                    bot.send_message(query.message.chat_id, 'Напишите ваш ответ')
                    your_self = True
                else:
                    otvet += str(query.data).split('+')[1] + '^^^^'
                    try:
                        bot.edit_message_caption(message_id=query.message.message_id,
                                                 caption="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                                 chat_id=query.message.chat_id)
                    except:
                        bot.edit_message_text(message_id=query.message.message_id,
                                              text="Ваш ответ: %s" % (str(query.data).split('+')[1]),
                                              chat_id=query.message.chat_id)
                    re = ''
                    te.append('####@LOVEISMYLOVE@')
                    try:
                        while ('####' not in te[I]):
                            re += te[I] + '\n'
                            I += 1
                        bot.send_message(query.message.chat.id, text=re)
                    except:
                        pass
                    u = te[I].split('####')
                    if u[-1] != '@LOVEISMYLOVE@':
                        if u[0] != 'NOOO':
                            photo = u[0]
                            re = u[1]
                            answers = u[-1].split('$')
                            bottons = []
                            for i in range(len(answers)):
                                botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                                bottons.append(botton)
                            reply_markup = InlineKeyboardMarkup(bottons)
                            bot.send_photo(query.message.chat.id, photo=photo, caption=re, reply_markup=reply_markup)
                        else:
                            re = u[1]
                            answers = u[-1].split('$')
                            bottons = []
                            for i in range(len(answers)):
                                botton = [InlineKeyboardButton(answers[i], callback_data=str(I) + '+' + answers[i])]
                                bottons.append(botton)
                            reply_markup = InlineKeyboardMarkup(bottons)
                            bot.send_message(query.message.chat.id, text=re, reply_markup=reply_markup)
                    else:
                        con_keyboard = KeyboardButton(text="Отправить контакт", request_contact=True)
                        custom_keyboard = [[con_keyboard]]
                        reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
                        bot.sendMessage(query.message.chat_id, text="Для окончания опроса нужен ваш номер телефона",
                                        reply_markup=reply_markup)
            except:
                try:
                    bot.edit_message_caption(message_id=query.message.message_id,
                                             caption="Ваш ответ: {}".format(query.data), chat_id=query.message.chat_id)
                except:
                    bot.edit_message_text(message_id=query.message.message_id, text="Ваш ответ: {}".format(query.data),
                                          chat_id=query.message.chat_id)
                # bot.send_photo(message.chat.id, photo = photo)
                bottons = [['Скорочтение'], ['Робототехника'], ['Арифметика'], ['Свяжитесь с нами']]
                if base_w.set_razdel() != None:
                    bottons.append(['Получить скидку'])
                keyboard = ReplyKeyboardMarkup(bottons, resize_keyboard=True)
                bot.send_message(query.message.chat.id, 'Спасибо за ваш голос', reply_markup=keyboard)
                for i in constants.admins:
                    try:
                        bot.send_message(i, 'Имя: ' + query.message.chat.username + '\nНомер телефона: +' + str(
                            base_w.select_number(query.message.chat.id)[0]) + '\nОтвет: ' + str(query.data))
                    except:
                        pass

    except:
        pass


start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.all, answer_questions)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling(timeout=5, clean=True)
