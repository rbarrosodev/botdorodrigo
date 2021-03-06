import telebot
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

time.clock = time.time

chatbot = ChatBot("BotRodrigo")
conversa = [
    "Como você está?",
    "Bem",
    "Que ótimo",
    "Feliz",
    "Que ótimo",
    "Alegre",
    "Que ótimo",
    "Mal",
    "Poxa, que triste amigo",
    "Triste",
    "Poxa, que triste amigo",
    "Cansado",
    "Poxa, que triste amigo",
    "oi",
    "oi, tudo bem?",
    "tudo, e você?",
    "tudo bem também",
    "qual a boa de hoje?",
    "a boa de hoje é trabalhar",
    "caraca que doidera",
    "pois é né",
    "tamo junto",
    "tamo junto patrão",
    "Qual é o seu nome?",
    "Meu nome é bot do Rodrigo!"
]

API_KEY = "5367731532:AAH5z61S8BRVrqltgUgrHR1YD6PV_Fy2TqQ"

bot = telebot.TeleBot(API_KEY)

#trainer = ListTrainer(chatbot)
#trainer.train(conversa)


def verificar(msg):
    print(msg.from_user.first_name)
    match msg.text:
        case "/start":
            responder(msg)
        case "/opcao1":
            show_temp_rio(msg)
        case "/opcao2":
            show_temp_nit(msg)
        case "/opcao3":
            show_brasilia_time(msg)
        case _:
            answer(msg)


@bot.message_handler(func=verificar)
def responder(msg):
    text = f"""Oi {msg.from_user.first_name}, eu sou o bot de Teste do Rodrigo, fui criado apenas para testes. 
                Escolha uma opção para eu te ajudar :) (Clique no item):
                /opcao1 Dizer a temperatura atual no Rio de Janeiro
                /opcao2 Dizer a temperatura atual em Niterói
                /opcao3 Mostrar o horário oficial de Brasília
                ou apenas converse comigo ;)"""
    bot.reply_to(msg, text)


def show_temp_rio(msg):
    text = "A temperatura atual no Rio é 27ºC."
    bot.reply_to(msg, text)


def show_temp_nit(msg):
    text = "A temperatura atual em Niterói é 28ºC."
    bot.reply_to(msg, text)


def show_brasilia_time(msg):
    cur_time = datetime.now().strftime("%H:%M")
    text = f"O horário atual de Brasília é {cur_time}"
    bot.reply_to(msg, text)


def answer(msg):
    bot.reply_to(msg, chatbot.get_response(msg.text))

bot.polling()