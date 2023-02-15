#May Omnissiah forgive me my sins and bless this code. Amen.

import random
import time
import telegram.ext
import requests

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from random import randint
from time import sleep


Token = "INSERT YOUR TOKEN HERE"

updater = telegram.ext.Updater("INSERT YOUR TOKEN HERE", use_context=True)
dispatcher = updater.dispatcher

events = ['Раптово відкрився портал у варп і з нього висипались орочі бойзи!',
          'Щойно ваші ауспекси зафіксували тиранідський живий корабель у безпосередній близості. І як він підійшов непоміченим?..',
          'Почався варп-шторм! Всі наступні спроби використати психічні сили можуть призвести до непередбачуваних наслідків.',
          'Біля вас відкрився портал у варп і з нього випала купа металобрухту. У ній ви розгледіли запечатаний ящик з боєприпасами.',
          'Відкрився портал у варп і з нього вилетіли демони! Непощастило так непощастило.',
          'Біля вас відкрився портал в варп і з нього вийшов хаоситський титан класу "Гончак". КАПІТАЛЬНО непощастило.']

enemiesOrks0 = ['1 мекбойз', '1 варбосс', 'банка-убивця', '1 горканавт', '1 вартракк']
enemiesOrks1 = ['2 бойзи з чоппами', '3 бойзи з вогнеметами', '3 гретчини', '2 вибухових сквіга', '5 снотлінгів']

enemiesTyranids0 = ['1 тиран вулика', '1 зоантроп', '1 гарпія', '1 маліцептор']
enemiesTyranids1 = ['2 ліктори', '3 гаунти', '2 пожирачі']

enemiesChaos0 = ['1 Кровожер', '1 Великий Нечистий', 'Пекельний дракон', '3 психноєни', '1 Осквернювач']
enemiesChaos1 = ['2 жахи Тзінча', '3 гончака Кхорна', '2 демонетки Слаанеш', '5 нурглінгів']


lootOrks = ['Купа непотрібного металобрухту',
            '1 чоппа. Можна вдарити когось',
            '1 дакка. Стріляє лише в орочіх руках',
            'Ороче м*ясо. Якщо вам більше нічого їсти...']
lootTyranids = ['1 клешня. Достатньо гостра.',
                '2 шматки тиранідського м*яса. Краще не їсти',
                '1 півметровий кіготь. Якщо ви загубили свій ніж - саме те',
                'Калюжа кислотної крові. Достатньо щоб розплавити щось або когось.',
                'Вцілілий шматок панцира. Може витримати ще кілька попадань з болтера.']
lootChaos = ['1 дивна книга на замку. Якимось чином не дематеріалізувалась',
             '1 невеликий камінець. Переливається всіма кольорами райдуги',
             'Калюжа сірої жижи. Смердить огидно.',
             'Хмара синього туману. Близько підходити не рекомендується',
             '1 короткий меч зі склоподібної аморфної речовини. Використовувати на свій страх і ризик.']
lootImperium = ['2 крак-гранати',
                '2 фраг-гранати',
                '1 лазган',
                '1 ніж',
                '2 повних магазини набоїв для болтера',
                'Купа металобрухту',
                '1 стаббер',
                '1 мельта-бомба',
                '1 плазмовий пістолет',
                '3 повних магазини набоїв для стаббера',
                '1 болт-пістолет',]

def start(update, context):
    update.message.reply_text("Ваш мікропомічник у веденні ваховських кампаній.")

def rollD3(update, context):
    txmsg = randint(1, 3)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollD4(update, context):
    txmsg = randint(1, 4)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollD6(update, context):
    txmsg = randint(1, 6)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollD8(update, context):
    txmsg = randint(1, 8)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollD10(update, context):
    txmsg = randint(1, 10)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollD20(update, context):
    txmsg = randint(1, 20)
    context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def rollCoin(update, context):
    x = randint(0, 1)
    if x == 0:
        txmsg = "Орел"
        context.bot.sendMessage(chat_id='-858506491', text=txmsg)
    else:
        txmsg = "Решка"
        context.bot.sendMessage(chat_id='-858506491', text=txmsg)

def startEvents(update, context):
    x = randint(0, 5)
    if x == 0:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[0], photo='https://warhammergames.ru/_pu/0/50128183.jpg')
        context.bot.sendMessage(chat_id='-858506491', text="Вороги:")
        a = random.choice(enemiesOrks1)
        b = random.choice(enemiesOrks1)
        if a == b:
            while a == b:
                b = random.choice(enemiesOrks1)
            tmsg = random.choice(enemiesOrks0) + ", " + a + ", " + b
            context.bot.sendMessage(chat_id='-858506491', text=tmsg)
        else:
            tmsg = random.choice(enemiesOrks0) + ", " + a + ", " + b
            context.bot.sendMessage(chat_id='-858506491', text=tmsg)
    elif x == 1:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[1], photo='https://qph.cf2.quoracdn.net/main-qimg-f4c9f3f2fa0860fdc271fd07a4bb41f8-pjlq')
        context.bot.sendMessage(chat_id='-858506491', text="Вороги:")
        tmsg = random.choice(enemiesTyranids0) + ", " + random.choice(enemiesTyranids1)
        context.bot.sendMessage(chat_id='-858506491', text=tmsg)
    elif x == 2:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[2], photo='https://static.wikia.nocookie.net/warhammer40k/images/3/36/Waves_of_the_Warp.jpg/revision/latest?cb=20190609035307&path-prefix=ru')
        context.bot.sendMessage(chat_id='-858506491', text="Вплив нестабільних психічних хвиль:")
        x = randint(0, 1)
        if x == 0:
            context.bot.sendMessage(chat_id='-858506491', text="Психічні сили всіх псайкерів, навігаторів і астропатів посилені")
        else:
            context.bot.sendMessage(chat_id='-858506491', text="Психічні сили всіх псайкерів, навігаторів і астропатів послаблені")
    elif x == 3:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[3], photo='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/49cce9df-878d-4485-acdb-061404f21389/dbnx5f1-227d95f1-d9c4-4666-b55d-af2626623c4f.png/v1/fill/w_1024,h_919,q_80,strp/warhammer_40k___ammo_box___part_1_by_marthendal_dbnx5f1-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTE5IiwicGF0aCI6IlwvZlwvNDljY2U5ZGYtODc4ZC00NDg1LWFjZGItMDYxNDA0ZjIxMzg5XC9kYm54NWYxLTIyN2Q5NWYxLWQ5YzQtNDY2Ni1iNTVkLWFmMjYyNjYyM2M0Zi5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.uBbFji38g8kyz88ZHBlZanBqNaqS0jtHkufQeKKZDsA')
    elif x == 4:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[4], photo='https://www.belloflostsouls.net/wp-content/uploads/2018/01/60030115006_CodexChaosDaemonsENG02-e1524631810460.jpg')
        context.bot.sendMessage(chat_id='-858506491', text="Вороги:")
        tmsg = random.choice(enemiesChaos0) + ", " + random.choice(enemiesChaos1)
        context.bot.sendMessage(chat_id='-858506491', text=tmsg)
    elif x == 5:
        context.bot.sendPhoto(chat_id='-858506491', caption=events[5], photo='https://64.media.tumblr.com/648f5486db45399e2d7a7ed06bdc1ca7/tumblr_pan8rlxXsq1uym32uo1_640.jpg')
    else:
        context.bot.sendMessage(chat_id='-858506491', text="Виникла помилка, усуваю скрапкод.")

def lootboxOrks(update, context):
    tmsg = random.choice(lootOrks) + ", " + random.choice(lootOrks)
    context.bot.sendMessage(chat_id='-858506491', text=tmsg)

def lootboxTyranids(update, context):
    tmsg = random.choice(lootTyranids)
    context.bot.sendMessage(chat_id='-858506491', text=tmsg)

def lootboxChaos(update, context):
    tmsg = random.choice(lootChaos)
    context.bot.sendMessage(chat_id='-858506491', text=tmsg)

def lootboxImperium(update, context):
    tmsg = random.choice(lootImperium) + ", " + random.choice(lootImperium) + ", " + random.choice(lootImperium)
    context.bot.sendMessage(chat_id='-858506491', text=tmsg)


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))

dispatcher.add_handler(telegram.ext.CommandHandler('rollD3', rollD3))
dispatcher.add_handler(telegram.ext.CommandHandler('rollD4', rollD4))
dispatcher.add_handler(telegram.ext.CommandHandler('rollD6', rollD6))
dispatcher.add_handler(telegram.ext.CommandHandler('rollD8', rollD8))
dispatcher.add_handler(telegram.ext.CommandHandler('rollD10', rollD10))
dispatcher.add_handler(telegram.ext.CommandHandler('rollD20', rollD20))
dispatcher.add_handler(telegram.ext.CommandHandler('rollCoin', rollCoin))

dispatcher.add_handler(telegram.ext.CommandHandler('startEvents', startEvents))

dispatcher.add_handler(telegram.ext.CommandHandler('lootboxOrks', lootboxOrks))
dispatcher.add_handler(telegram.ext.CommandHandler('lootboxTyranids', lootboxTyranids))
dispatcher.add_handler(telegram.ext.CommandHandler('lootboxChaos', lootboxChaos))
dispatcher.add_handler(telegram.ext.CommandHandler('lootboxImperium', lootboxImperium))

updater.start_polling()
updater.idle()