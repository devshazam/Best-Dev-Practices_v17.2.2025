# from django.shortcuts import render
# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse

import telebot
from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth
import base64
import json 
import random 
import uuid
from telebot.types import LabeledPrice, ShippingOption
from telebot import types # для указание типов
import os
from .models import Orders
# from dotenv import load_dotenv
# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather
# from members.models import Journal, Errors
import datetime
# import logging
# from systemd import journal
# log = logging.getLogger('demo')
# log.addHandler(journal.JournaldLogHandler())
# log.setLevel(logging.INFO)
from dotenv import load_dotenv

import re
from .config.goods import goodsArray

from django.views.decorators.csrf import csrf_exempt


# bot = telebot.TeleBot(settings.BOT_TOKEN)
# bot = telebot.TeleBot("7397048375:AAFUc0nI6IQpsIgIWWW6ccU-gkgKSrLkMKQ")
# https://api.telegram.org/bot7397048375:AAFUc0nI6IQpsIgIWWW6ccU-gkgKSrLkMKQ/setWebhook?url=https://201e-80-90-179-8.ngrok-free.app/
# https://api.telegram.org/bot7397048375:AAFUc0nI6IQpsIgIWWW6ccU-gkgKSrLkMKQ/deleteWebhook?url=https://089e-80-90-179-8.ngrok-free.app/


# CONFIG

costOfBannerArray = [550, 500, 400, 350, 300, 280, 240]
costOfLuvers = 15
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

user_state_data = {}
ADMIN_CHAT_ID = "6128389355"






def members(request):
    bot.send_message(ADMIN_CHAT_ID,'Это сосбщение отджанго - прямое! ')
    return HttpResponse("Hello world!")




def payForGoods(request):
    load_dotenv()
    MARKET_ID = os.getenv("MARKET_ID")
    SECRET_KEY_UMONEY = os.getenv("SECRET_KEY_UMONEY")

    print(1, MARKET_ID, SECRET_KEY_UMONEY)
    
    cost = request.POST.get("cost")
    userId = request.POST.get("userId")
    description = request.POST.get("description")

    
    print(1, cost, userId)
    
    IdempotenceKey = uuid.v4()
    encode_login = base64.b64encode(bytes(MARKET_ID + ":" + SECRET_KEY_UMONEY , 'utf8'))
    headers={
        "Content-Type": "application/json",
        "Idempotence-Key": IdempotenceKey,
        'Authorization': "Basic " + encode_login.decode(),
    }

    inputBody = {
        'amount': { 'value': f'{cost}', 'currency': "RUB", },
        'capture': True,
        'confirmation': {
            'type': "redirect",
            'return_url': "https://telebot-app.kopi34.ru/", #TODO - поменять адрес
        },
        'description': f"Оплата из приложения Телеграмм, юзер: {userId}",
    }

    r=requests.post("https://api.yookassa.ru/v3/payments", headers, json=inputBody)
    print(r, r.json())

    newPay = Orders(payId=r.id, cost='cost', userChatTelegramId=userId, description=description)
    newPay.save()
    return JsonResponse(r) 





hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard



@csrf_exempt
def index(request):
    # bot.set_webhook('https://315f-80-90-179-8.ngrok-free.app/')
    # print(request)
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])

    return HttpResponse('<h1>Ты подключился!</h1>')










@bot.message_handler(commands=['start'])
def clientId(message):
    try: 

        bot.send_message(message.chat.id, 'Здравствуйте дорогой Клиент!'
                                            '\nЯ Бот по приёму заказов'
                                            '\n') # Duplicate with a message that the user will now send his phone number to the bot (just in case, but this is not necessary)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))


@bot.message_handler(commands=['s'])
def clientId(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
        webApp = types.WebAppInfo("https://telebot-app.kopi34.ru/") #создаем webappinfo - формат хранения url
        webA = types.WebAppInfo("https://games.mihailgok.ru") #создаем webappinfo - формат хранения url
        one = types.KeyboardButton(text="Калькулятор Визиток", web_app=webApp) #создаем кнопку типа webapp
        two = types.KeyboardButton(text="Игра", web_app=webA) #создаем кнопку типа webapp
        keyboard.add(one, two) #добавляем кнопки в клавиатуру
        bot.send_message(message.chat.id, 'Вы выбрали визитки\nЗапустите калькуляторцуцукцуе!.', parse_mode="Markdown", reply_markup=keyboard) #отправляем сообщение с нужной клавиатурой
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, str(e))



@bot.callback_query_handler(func=lambda call: call.data == 'banner')
def startBanner(call):
    try:
        print(3234)
        message = call.message
        bot.clear_step_handler_by_chat_id(message.chat.id)
        mesg = bot.send_message(message.chat.id, 'Введите его длину в Миллиметрах:')
        bot.register_next_step_handler(mesg, loop1)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, str(e))

def loop1(message):
    try:
        print(1, message)
        x1 = re.search(r"\d+", message.text)
        if not x1 :
            raise Exception("Значение длинны не корректное! Начните заново!")
        x2 = int(x1.group())
        
        if x2 < 100 and x2 > 20000:
            raise Exception("Значение длинны меньше 100 или больше 20000 мм! Начните заново!")
        
        chat_id = message.chat.id
        user_state_data[f"{chat_id}_order"] = {'user': [message.chat.id, message.chat.first_name, message.chat.last_name], 'name': "Баннер", 'options': [x2], 'cost': 0, 'messages': []}

        print(user_state_data[f"{chat_id}_order"])

        mesg = bot.send_message(message.chat.id, 'Введите ширину в Миллиметрах:')
        bot.register_next_step_handler(mesg, loop2)

    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, str(e))

def loop2(message):
    try:
        x1 = re.search(r"\d+", message.text)
        if not x1 :
            raise Exception("Значение длинны не корректное! Начните заново!")
        x2 = int(x1.group())
        
        if x2 < 100 and x2 > 20000:
            raise Exception("Значение длинны меньше 100 или больше 20000 мм! Начните заново!")
            
        chat_id = message.chat.id
        user_state_data[f"{chat_id}_order"]['options'].append(x2)
        print(user_state_data[f"{chat_id}_order"])

        mesg = bot.send_message(message.chat.id,'Введите количество Баннеров в Штуках:')
        bot.register_next_step_handler(mesg, loop3)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, str(e))

def loop3(message):
    try:
        x1 = re.search(r"\d+", message.text)
        if not x1 :
            raise Exception("Значение длинны не корректное! Начните заново!")
        x2 = int(x1.group())
        
        if x2 == 0 and x2 > 100:
            raise Exception("Значение равно 0 или больше 100! Начните заново!")
            
        chat_id = message.chat.id
        user_state_data[f"{chat_id}_order"]['options'].append(x2)
        print(user_state_data[f"{chat_id}_order"])

        mesg = bot.send_message(message.chat.id,'Введите шаг люверсов в Миллиметрах (0, 200, 300, 400, 500):')
        bot.register_next_step_handler(mesg, loop4)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, str(e))
def loop4(message):
    try:
        x1 = re.search(r"\d+", message.text)
        if not x1 :
            raise Exception("Значение длинны не корректное! Начните заново!")
        x2 = int(x1.group())
        
        if int(x2) not in [0, 200, 300, 400, 500]:
            raise Exception("Значение не соответствует заданным шагам! Начните заново!")
            
        chat_id = message.chat.id
        user_state_data[f"{chat_id}_order"]['options'].append(x2)
        print(user_state_data[f"{chat_id}_order"])

        # Расчет стоимости баннера
        summ = user_state_data[f"{chat_id}_order"]['options'][0] * user_state_data[f"{chat_id}_order"]['options'][1] * user_state_data[f"{chat_id}_order"]['options'][2] / 1000000
        totalBannerCost = 0 
        if summ < 5:
            totalBannerCost = costOfBannerArray[0] * summ
        elif summ >= 5 and summ < 10:
            totalBannerCost = costOfBannerArray[1] * summ
        elif summ >= 10 and summ < 50:
            totalBannerCost = costOfBannerArray[2] * summ
        elif summ >= 50 and summ < 100:
            totalBannerCost = costOfBannerArray[3] * summ
        elif summ >= 100 and summ < 500:
            totalBannerCost = costOfBannerArray[4] * summ
        elif summ >= 500:
            totalBannerCost = costOfBannerArray[5] * summ
        totalLuversCost = round(((user_state_data[f"{chat_id}_order"]['options'][0] + user_state_data[f"{chat_id}_order"]['options'][1]) * user_state_data[f"{chat_id}_order"]['options'][2] * 2) / user_state_data[f"{chat_id}_order"]['options'][3]) * costOfLuvers
        user_state_data[f"{chat_id}_order"]['cost'] = totalBannerCost + totalLuversCost
        # Расчет стоимости баннера

        print(user_state_data[f"{chat_id}_order"])

        mesg = bot.send_message(message.chat.id, f'Цена: {user_state_data[f"{chat_id}_order"]['cost']} рублей\nЕсли Вас все устраивает, то добавьте описание или файл')
        bot.register_next_step_handler(mesg, loop5)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))

def loop5(message):
    try:
        chat_id = message.chat.id
        user_state_data[f"{chat_id}_order"]['messages'].append(["1449707152", message.message_id, chat_id])
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_save = telebot.types.InlineKeyboardButton(text="Оплатить",
                                                        callback_data='pay')
        button_change = telebot.types.InlineKeyboardButton(text="Добавить описание или файл",
                                                        callback_data='pay')
        keyboard.add(button_save, button_change)
        print(user_state_data[f"{chat_id}_order"])
        
        mesg = bot.send_message(message.chat.id, f'Цена: {user_state_data[f"{chat_id}_order"]['cost']} рублей\nДлинна баннера: {user_state_data[f"{chat_id}_order"]['options'][0]}\nШирина баннера: {user_state_data[f"{chat_id}_order"]['options'][1]}\nКол-во баннеров: {user_state_data[f"{chat_id}_order"]['options'][2]}\nШаг люверсов: {user_state_data[f"{chat_id}_order"]['options'][3]}\n', reply_markup=keyboard)
        # bot.register_next_step_handler(mesg, loop5)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))


@bot.callback_query_handler(func=lambda call: call.data == 'pay')
def save_btn(call):
    try:
        print(1)
        message = call.message
        chat_id = message.chat.id
        message_id = message.message_id  
        # bot.edit_message_text(chat_id=chat_id, message_id=message_id, 
        #                      text='Данные сохранены!')  
        prices = [LabeledPrice(label='Working Time Machine', amount=57000)]
        print(2)

        what = bot.send_invoice(
            message.chat.id,  #chat_id
            'Заголовок за что оплата', #title
            'Описание за что оплата!', #description
            'HAPPY FRIDAYS COUPON', #invoice_payload
            '381764678:TEST:90012', #provider_token
            'rub', #currency
            prices, #prices # True If you need to set up Shipping Fee
            start_parameter='djfi834830fk0skfsdjsjkjjjjjjd09221-2-HHDLPSI')
        print(what)
        print(4)
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))

@bot.callback_query_handler(func=lambda call: call.data == 'add_data')
def save_btn(call):
     message = call.message
     bot.register_next_step_handler(message, loop5)


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(3)
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    print(pre_checkout_query)
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    print(message)
    bot.send_message(message.chat.id,
                     'Hoooooray! Thanks for payment! We will proceed your order for `{} {}` as fast as possible!',
                     parse_mode='Markdown')



# def loopGoods3(message):
#     try:
#         if message.text == 'rs':
#             bot.clear_step_handler_by_chat_id(message.chat.id)
#         else:
#             keyboard = telebot.types.InlineKeyboardMarkup()
#             button_save = telebot.types.InlineKeyboardButton(text="Сохранить",
#                                                             callback_data='save_data')
#             button_change = telebot.types.InlineKeyboardButton(text="Изменить",
#                                                             callback_data='change_data')
#             keyboard.add(button_save, button_change)

#             bot.send_message(chat_id, f'Сохранить данные?', reply_markup=keyboard)

#     except Exception as e:      # works on python 3.x
#         print('Failed 5: %s', repr(e))
#         Errors.objects.create(description=str(e))

# def switch(message):
#     try:
#         if message.text == 'rs':
#             bot.clear_step_handler_by_chat_id(message.chat.id)
#         else:
#             chat_id = message.chat.id

#             if message.text == 'Добавить товар!':
#                 x1 = 'Введенная строка \n'
#                 for x in clientArray[1][len(clientArray[1]) - 1]:
#                     x1 += str(x) + '\n'
#                 bot.send_message(message.chat.id, x1)
#                 mesg = bot.send_message(message.chat.id,'Введите наименование нового товара')
#                 bot.register_next_step_handler(mesg,loopGoods1)

#             elif message.text == 'Генероривать документ!':
#                 todayDate = datetime.datetime.today().strftime("%d%m%y")
#                 print(1, type(todayDate), todayDate)
#                 x1 = None

#                 if Journal.objects.filter(name=todayDate).exists():
#                     getDay = Journal.objects.filter(name=todayDate).get()
#                     x1 = int(getDay.number) + 1
#                     getDay.number = x1
#                     getDay.save()
#                     # Journal.objects.filter(name=todayDate).update(number=(int(x1) + 1))
#                 else:
#                     Journal.objects.create(name=todayDate, number=1)
#                     x1 = 1

#                 bot.send_document(message.chat.id, mymodule.word_generate(clientArray, x1), visible_file_name='счет.docx')
#                 bot.send_document(message.chat.id, mymodule2.word_generate(clientArray, x1), visible_file_name='акт приемки.docx')

#             else:
#                 bot.send_message(message.chat.id,'Ошибка, начните заново с команды /start !')
#     except Exception as e:      # works on python 3.x
#         print('', repr(e))
#         bot.send_message(message.chat.id, 'Данные введены не корректно.'
#                                           '\nПопробуйте еще разок, вводите данные рукой.')
#         Errors.objects.create(description=str(e))
   





# forward_message(chat_id: int | str, from_chat_id: int | str, message_id: int





@bot.message_handler(regexp=r"визитка")
def start_fun(message):
    try:
       
        print(324)
        keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
        webApp = types.WebAppInfo("https://dev2.kopi34.ru/cards") #создаем webappinfo - формат хранения url
        webA = types.WebAppInfo("https://games.mihailgok.ru") #создаем webappinfo - формат хранения url
        one = types.KeyboardButton(text="Калькулятор Визиток", web_app=webApp) #создаем кнопку типа webapp
        two = types.KeyboardButton(text="Игра", web_app=webA) #создаем кнопку типа webapp
        keyboard.add(one, two) #добавляем кнопки в клавиатуру
        bot.send_message(message.chat.id, 'Вы выбрали визитки\nЗапустите калькуляторцуцукцуе!.', parse_mode="Markdown", reply_markup=keyboard) #отправляем сообщение с нужной клавиатурой
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))




@bot.message_handler (commands = ['number']) # Announced a branch to work on the <strong> number </strong> command
def phone (message):
    keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True) # Connect the keyboard
    button_phone = types.KeyboardButton (text = "Разрешить!", request_contact = True) # Specify the name of the button that the user will see
    keyboard.add (button_phone) #Add this button
    bot.send_message (message.chat.id, 'Пожалуйста, разрешите доступ к вашему номеру телефона для возможности уточнить информацию!', reply_markup = keyboard) # Duplicate with a message that the user will now send his phone number to the bot (just in case, but this is not necessary)
 
@bot.message_handler (content_types = ['contact']) # Announced a branch in which we prescribe logic in case the user decides to send a phone number :)
def contact (message):
    if message.contact is not None: # If the sent object <strong> contact </strong> is not zero
        print (message.contact) # We display the contact





@bot.callback_query_handler(func=lambda call: call.data == 'photo')
def startBanner(call):
    try:
        message = call.message
        bot.send_photo(message.chat.id, photo=open(fr'{os.path.dirname(os.path.abspath(__file__))}\static\123.jpg', 'rb'), caption="Перейдите в Магазин, пожалуйста!")
    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))






@bot.message_handler(content_types=['text'])
def func(message):
    try:
        x1 = 0
        for x in goodsArray:
            if re.search(fr"{x[0]}", message.text, re.IGNORECASE):

                keyboard = telebot.types.InlineKeyboardMarkup()
                button_save = telebot.types.InlineKeyboardButton(text=f"Подтвердить!", callback_data=f"{x[2]}")
                keyboard.add(button_save)
                bot.send_message(message.chat.id, f'Вы выбрали {x[1].capitalize()}?', reply_markup=keyboard)
                x1 = 1

                break

        if x1 == 0:
            bot.send_message(message.chat.id, 'Извините! На такую комманду я не запрограммирован.')

    except Exception as e:      # works on python 3.x
        print('Error №1 -', repr(e))
        bot.send_message(message.chat.id, str(e))



