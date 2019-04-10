# coding: utf-8
import os
import telebot
from agenda import get_consulta, get_agenda
  
bot = telebot.TeleBot('746873066:AAEjeZo1uTs9dtW5lA5k4O71tvEitV2eXsQ')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!\nPara agendar: /agendar\nPara Consultar disponibilidade de horario: /consulta")

@bot.message_handler(commands=['agendar'])
def send_league_data(message):
    bot.reply_to(message, get_agenda())


@bot.message_handler(commands=['consulta'])
def send_partials(message):
    bot.reply_to(message, get_consulta())

bot.polling()
