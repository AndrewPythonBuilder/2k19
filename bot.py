import constants
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import user_com
from datetime import time
import random
flag = False
time_you = False
money = False
money_1 = False
const = False
const_1 = False
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher
job_queue = updater.job_queue



def start (bot, update):
    if update.message.chat.id == constants.admin or update.message.chat.id == constants.admin2:
        bottons = [['Закинуть деньги', 'Прибавить деньги игроку']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                     'Доброго времени суток, админ', reply_markup=user_markup)
    else:
        global flag ,time_you, money, money_1
        link_name = str(update.message.text)[7:]
        hello = user_com.registration(update.message.chat.id, update.message.chat.first_name, str(update.message.chat.id),
                                      link_name)
        time_you = False
        flag = False
        money = False
        money_1 = False
        bottons = [['💰Пополнить баланс', '🤝Пари'],
                   ['💸Вывести средства', '💼Мой баланс'],
                   ['🔥Дополнительно']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(chat_id=update.message.chat_id, text=constants.hello_text, reply_markup=user_markup)

def answer_start(bot, update):
    global flag, time_you, money, money_1, const, const_1
    if update.message.text == '💰Пополнить баланс':
        bottons = [['Bitcoin- btc', 'Etherium - eth'],['Yandex Money'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, ' Выберите метод пополнения⬇️')
        bot.send_message(update.message.chat.id, 'Любой из методов пополнения будет автоматичекси конвертирован в BTC.',
                         reply_markup=user_markup)
        bot.send_message(constants.admin,
                         str(update.message.chat.id) + ' это id человека, который нажал "Пополнить баланс"')
    elif update.message.text == '💼Мой баланс':
        id_ = update.message.chat.id
        s = str(user_com.info(id_)[2])
        bot.send_message(update.message.chat.id, 'Ваш баланс ' + s + ' ВТС')
    elif update.message.text == '🔥Дополнительно':
        bottons = [['Задать вопрос', 'Рефералы'], ['FAQ'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, '🔥Дополнительно', reply_markup=user_markup)
    elif update.message.text == '🤝Пари':
        bottons = [['BTC/USD', 'ETH/USD'], ['XRP/USD', 'BCC/USD'], ['EOS/USD', 'LTC/USD'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, 'Выберете нужную вам пару:', reply_markup= user_markup)
    elif update.message.text == '💸Вывести средства':
        bottons = [['Bitcоin- btc', 'Еtherium - eth'], ['Yаndex Money'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите валюту в которой вы хотите вывести средства.', reply_markup=user_markup)
    elif update.message.text == 'Bitcоin- btc' or update.message.text == 'Еtherium - eth' or update.message.text == 'Yаndex Money':
        const = True
        bot.send_message(update.message.chat.id, 'Введите номер кошелька: ')
    elif const == True:
        bot.send_message(update.message.chat.id, 'Введите сумму, которую вы желаете вывести. (Минимальная сумма 0,002 btc или  0.05 eth)')
        const = False
        const_1 =True
    elif const_1 == True:
        const_1 = False
        try:
            float(update.message.text)
            bot.send_message(update.message.chat.id, 'Не хватает денег')
        except:
            bot.send_message(update.message.chat.id, 'Что-то пошло не так, попробуйте еще раз')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif  update.message.text == 'BCC/USD':
        money = user_com.parse('BCC')
        constants.valume = 'BCC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс BCC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif  update.message.text == 'BTC/USD':
        money = user_com.parse('BTC')
        constants.valume = 'BTC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс BTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'ETH/USD':
        money = user_com.parse('ETH')
        constants.valume = 'ETH'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, ' Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс ETH: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'XRP/USD':
        money = user_com.parse('XRP')
        constants.valume = 'XRP'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс XRP: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'EOS/USD':
        money = user_com.parse('EOS')
        constants.valume = 'EOS'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс EOS: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'LTC/USD':
        money = user_com.parse('LTC')
        constants.valume = 'LTC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс LTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'Bitcoin- btc':
        bottons = [['Оплатил', 'Отмена']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.btc_text + '\n' + str(random.choice(constants.btc_list)), reply_markup=user_markup)
    elif update.message.text == 'Etherium - eth':
        bottons = [['Оплатил', 'Отмена']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, constants.eth_text + '\n' + str(random.choice(constants.eth_list)), reply_markup= user_markup)
    elif update.message.text == '1 Час':
        time_you = True
        user_com.set_alarm(1, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '2 Часа':
        time_you = True
        user_com.set_alarm(2, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '4 Часа':
        time_you = True
        user_com.set_alarm(4, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '6 Часов':
        time_you = True
        user_com.set_alarm(6, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '12 Часов':
        time_you = True
        user_com.set_alarm(12, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '24 Часа':
        time_you = True
        user_com.set_alarm(23, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == 'Вверх📈':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'more', money, constants.valume)
        except:
            pass
        bottons = [['1 Час', '2 Часа', '4 Часа'], ['6 Часов', '12 Часов', '24 Часа'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите нужное вам время:', reply_markup=user_markup)
    elif update.message.text == 'Вниз📉':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'less', money, constants.valume)
        except:
            pass
        bottons = [['1 Час', '2 Часа', '4 Часа'], ['6 Часов', '12 Часов', '24 Часа'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите нужное вам время:', reply_markup=user_markup)
    elif update.message.text == 'Назад': #Изменить приветствие
        flag = False
        time_you = False
        money = False
        money_1 = False
        bottons = [['💰Пополнить баланс', '🤝Пари'],
                   ['💸Вывести средства', '💼Мой баланс'],
                   ['🔥Дополнительно']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(chat_id=update.message.chat_id, text = random.choice(constants.hey_text), reply_markup=user_markup)
    elif update.message.text == 'Рефералы':
        info = user_com.info(update.message.chat.id)
        bot.send_message(update.message.chat.id, 'За каждого приведенного реферала, который пополнит баланс, вам начислится 0,0005 BTC \n Это ваша реферальная ссылка: http://t.me/Btc_winbot?start=' + str(info[3]) + ' . \n Ваши рефералы: ' + str(info[5]))
    elif update.message.text== 'Задать вопрос':

        flag = True
        bot.send_message(update.message.chat.id, 'Напишите ваш вопрос, в ближайшее время на него ответит наш модератор!')
    elif flag == True:
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        flag = False
        bot.send_message(update.message.chat.id, 'Спасибо')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif time_you == True:
        try:
            q = float(update.message.text)
            if  q <= user_com.info(update.message.chat.id)[2]:
                user_com.add_plus(update.message.chat.id, -q)
                user_com.pay(update.message.chat.id, q)
                bot.send_message(update.message.chat.id, 'Ставка принята')
                bot.send_message(constants.admin, str(q)+ ' '+ str(update.message.chat.id) )

            else:
                bot.send_message(update.message.chat.id, 'Не хватает денег')
            time_you = False
            update.message.text = 'Назад'
            answer_start(bot, update)

        except:
            time_you = False
            bot.send_message(update.message.chat.id, 'Что-то пошло не так')
            update.message.text = 'Назад'
            answer_start(bot, update)
    elif update.message.text == 'Закинуть деньги' and (update.message.chat.id == constants.admin or update.message.chat.id == constants.admin2 ):
        bot.send_message(update.message.chat.id, 'Какую сумму вы хотите закинуть? и какой id у пользователя?')
        bot.send_message(update.message.chat.id, 'Сначала вы пишите id человека, которому вы хотите закинуть денег, потом, через пробел сколько денег.')
        bot.send_message(update.message.chat.id, 'Например')
        bot.send_message(update.message.chat.id, '286077227 123')
        bot.send_message(update.message.chat.id, 'Теперь у человека id  которого 286077227  на счете 123 BTC')
        bot.send_message(update.message.chat.id, '!!! Главное. Эта Кнопка не прибавляет денег, а изменяет кол-во! То есть у человека было 12 BTC,  а после этой операции станет 123. Например !!!')
        bot.send_message(update.message.chat.id, 'Итак. Какую сумму вы хотите закинуть? и какой id у пользователя?')
        money = True
    elif money == True:
        try:
            text = update.message.text.split()
            user_com.add(text[1], text[0])
            bot.send_message(update.message.chat.id, 'Спасибо, деньги в игре')
            money = False
        except:
            bot.send_message(update.message.chat.id, 'Неверный формат')
            money = False
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif update.message.text == 'Прибавить деньги игроку':
        bot.send_message(update.message.chat.id, 'На сколько вы хотите увеличить счет игрока? и какой id у пользователя?')
        bot.send_message(update.message.chat.id,
                         'Сначала вы пишите id человека, которому вы хотите закинуть денег, потом, через пробел сколько денег.')
        bot.send_message(update.message.chat.id, 'Тут Вы прибавляете некую сумму на чей-то id')
        money_1 = True
    elif money_1 == True:
        try:
            text = update.message.text.split()
            user_com.add_plus(int(text[1]), int(text[0]))
            bot.send_message(update.message.chat.id, 'Спасибо, деньги в игре')


        except:
            bot.send_message(update.message.chat.id, 'Неверный формат')
        update.message.text = 'Назад'
        answer_start(bot, update)
        money_1 = False
    elif update.message.text == 'FAQ':
        bot.send_message(update.message.chat.id, constants.FAQ)
    elif update.message.text == 'Оплатил':
        bot.send_message(update.message.chat.id, 'Оплата принята, ваша транзакция находится в обработке, средства поступят к вам на счёт автоматически после 1-го подтверждения сети.')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif update.message.text == 'Отмена':
        update.message.text = 'Назад'
        answer_start(bot, update)
    s = user_com.o_clock()
    if s != []:
        for i in s:
            info = user_com.info(i)
            try:
                money_l = user_com.parse(i)
            except:
                break
            if info[8] == 'less':
                if float(str(money_l)) < float(info[7]):
                    user_com.add_plus(info[0], info[6] * 1.8)
                    bot.send_message(info[0], 'Ставка прошла')
                else:
                    bot.send_message(info[0], 'Ставка не прошла')
            else:
                if float(str(money_l)) > float(info[7]):
                    user_com.add_plus(info[0], info[6] * 1.8)
                    bot.send_message(info[0], 'Ставка прошла')
                else:
                    bot.send_message(info[0], 'Ставка не прошла')
            user_com.null(info[0])




def question(bot,update):
    print(update.message.text)


def time_now(bot, arg):
    global flag, time_you, money, money_1,const, const_1
    time_you = flag =  money_1 =  money = const = const_1 = False
    id_ = user_com.all_id()
    write = user_com.parse('All')
    for j in id_:
        try:
            bot.send_message(j[0], constants.kurs % (write[0], write[1], write[2], write[3], write[4], write[6]))
            bottons = [['BTC/USD', 'ETH/USD'], ['XRP/USD', 'BCC/USD'], ['EOS/USD', 'LTC/USD'], ['Назад']]
            user_markup = ReplyKeyboardMarkup(bottons)
            bot.send_message(j[0], 'Выберете нужную вам пару:', reply_markup=user_markup)
        except:
            pass




question_handler = CommandHandler('question', question)
start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, answer_start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(question_handler)
job_queue.run_daily(time_now, time(22,00))
job_queue.run_daily(time_now, time(18,00))
job_queue.run_daily(time_now, time(21,00))
job_queue.run_daily(time_now, time(20,00))
job_queue.run_daily(time_now, time(16,00))
job_queue.run_daily(time_now, time(14,00))
job_queue.run_daily(time_now, time(12,00))
job_queue.run_daily(time_now, time(10,00))
job_queue.run_daily(time_now, time(8,00))
job_queue.run_daily(time_now, time(6,00))
job_queue.run_daily(time_now, time(4,00))
job_queue.run_daily(time_now, time(2,00))
job_queue.run_daily(time_now, time(0,00))
dispatcher.add_handler(answer_handler)
updater.start_polling(timeout=5, clean=True )
