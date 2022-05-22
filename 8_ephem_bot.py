"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

import datetime
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#planets=['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

#PROXY = {'proxy_url':settings.PROXY_URL,
    #'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /Start")
    #print(1/0)
    #print(update)
    update.message.reply_text('Здравствуй, Пользователь!')
    update.message.reply_text('Что бы узнать где находится небесное тело введите  /planet и любую планету из списка Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto. Например /planet Jupiter')

def talk_to_me(update, context):
    text =  update.message.text
    print(text)
    update.message.reply_text(text)

def where_is_planet(update, context):

    
    text = update.message.text
    
    planet_list = text.split()
    #print("got it", text, planet_list)
    planet_list.remove('/planet')
    #print("got it", text, planet_list)
    date = datetime.date.today()
    #print("got it", text, planet_list)
    #print(planet_list, date, "constellation")
    
    if planet_list[0].capitalize() == 'Sun':
        sun = ephem.Sun(date)
        constellation = ephem.constellation(sun)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
    
    elif planet_list[0].capitalize() == "Moon":
        moon = ephem.Moon(date)
        constellation = ephem.constellation(moon)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
    
    elif planet_list[0].capitalize() == "Mercury":
        mercury = ephem.Mercury(date)
        constellation = ephem.constellation(mercury)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
    
    elif planet_list[0].capitalize() == "Venus":
        venus = ephem.Venus(date)
        constellation = ephem.constellation(venus)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")

    elif planet_list[0].capitalize() == "Mars":
        mars = ephem.Mars(date)
        constellation = ephem.constellation(mars)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")

    elif planet_list[0].capitalize() == "Jupiter":
        jupiter = ephem.Jupiter(date)
        constellation = ephem.constellation(jupiter)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")

    elif planet_list[0].capitalize() == "Saturn":
        saturn = ephem.Saturn(date)
        constellation = ephem.constellation(saturn)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
    
    elif planet_list[0].capitalize() == "Uranus":
        uranus = ephem.Uranus(date)
        constellation = ephem.constellation(uranus)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
        #constellation = ephem.constellation(planet_list[0])
    

    elif planet_list[0].capitalize() == "Neptune":
        neptune = ephem.Neptune(date)
        constellation = ephem.constellation(neptune)
        print(constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")

    elif planet_list[0].capitalize() == "Pluto":
        pluto = ephem.Pluto(date)
        constellation = ephem.constellation(pluto)
        print(*constellation)
        update.message.reply_text(f"Введенная вами планета {planet_list[0]} находится сейчас в созвездии: {', '.join(constellation)}")
    else:
        update.message.reply_text("Планета неизвестна!")


    update.message.reply_text(planet_list, date, constellation)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)    #, request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', where_is_planet))
    
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, where_is_planet))

    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()