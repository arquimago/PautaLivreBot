#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

updater = Updater(token='COLOCA O TOKEN AQUI')
dispatcher = updater.dispatcher                                    

def start(bot, update):      
    bot.sendMessage(chat_id=update.message.chat_id, text="Este é o Bot da Pauta Livre, mande mensagens no horário da Pauta Livre elas serão enviadas!")

start_handler = CommandHandler('start', start)                   
dispatcher.add_handler(start_handler)                                                              

def snyder(bot, update):                                                                       
    bot.sendMessage(chat_id=update.message.chat_id, text="@JPaesN S2 Snyder")

snyder_handler = CommandHandler('snyder', snyder)                               
dispatcher.add_handler(snyder_handler)                                                                                                                                                 

def bobo(bot, update):
    nome=update.message.from_user.name
    texto="Eu acho que " + nome  + " é bobo"
    bot.sendMessage(chat_id=update.message.chat_id, text=texto)       

bobo_handler = CommandHandler('bobo', bobo)
dispatcher.add_handler(bobo_handler)

def discordo(bot, update):
    nome=update.message.from_user.name
    mensagem=update.message.text
    print(nome + " " + mensagem)

def messages(bot, update):
    nome=update.message.from_user.username
    if nome=='Arquimago':
        bot.sendMessage(chat_id=update.message.chat_id, text="Eu discordo do @"+ nome +"!")

message_handler = MessageHandler(Filters.text,messages)
dispatcher.add_handler(message_handler)

updater.start_polling()