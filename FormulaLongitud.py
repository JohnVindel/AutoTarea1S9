#Tarea 1 - Formula de Longitud
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['metros-centimetros', 'm-cm', 'centimetro', 'cm'])
def info(mensaje):
    bot.reply_to(mensaje, "cm = 1 * 100")
    print("Metros a Centimetros")

@bot.message_handler(commands=['kilometros-metros', 'km-m', 'metros', 'm'])
def info(mensaje):
    bot.reply_to(mensaje, "km = 1 * 1000")
    print("Kilometro a Metros")

@bot.message_handler(commands=['millas-kilometros', 'mi-km', 'kilometros', 'mi'])
def info(mensaje):
    bot.reply_to(mensaje, "mi = 1 * 1.609")
    print("Milla a Kilometro")

@bot.message_handler(commands=['pie-pulgada', 'ft-in', 'pulgadas', 'ft'])
def info(mensaje):
    bot.reply_to(mensaje, "ft = 1 * 12")
    print("Pie a Pilgada")

bot.polling()