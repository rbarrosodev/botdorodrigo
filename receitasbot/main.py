import telebot
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

time.clock = time.time

chatbot = ChatBot("ReceitasBot")

API_KEY = "5360555583:AAFSn9tEtOUDPAbAox9TAl0p14Ctx2Mjy18"

bot = telebot.TeleBot(API_KEY)


# trainer = ListTrainer(chatbot)
# trainer.train(conversa)

def verificar(msg):
    match msg.text:
        case "/start":
            first_answer(msg)
        case "/recomendacao":
            recomendation(msg)
        case "/refeicao":
            refeicao(msg)
        case "/salgado":
            salgado(msg)
        case "/poucotempo":
            poucotempo(msg)


@bot.message_handler(func=verificar)
def first_answer(msg):
    text = f"""Oi {msg.from_user.first_name}, eu sou seu assistente virtual do Receitas, estou aqui para te ajudar! \n
Já que você é vegetariano, recomendamos 3 receitas que esperamos que goste: \n
Tofu Salteado com Cogumelos e Vegetais:
https://receitas.globo.com/tofu-salteado-com-cogumelos-e-vegetais-gnt.ghtml \n
Suco verde:
https://receitas.globo.com/suco-verde-da-ana-maria-braga.ghtml \n
Bolo de Maçã:
https://receitas.globo.com/bolo-de-maca-gnt.ghtml \n
Mas se quiser preparar outra coisa, também posso te recomendar algo especialmente para você, 
através do comando /recomendacao"""
    bot.reply_to(msg, text)


def recomendation(msg):
    text = f"""Perfeito {msg.from_user.first_name}, para te auxiliar, preciso saber que tipo de receita
você quer preparar (Selecione uma opção abaixo):
/petisco para selecionar Petiscos
/lanche para selecionar Lanches
/refeicao para selecionar Refeições
ou
/almoco para selecionar receitas para o seu almoço
    """
    bot.reply_to(msg, text)


def refeicao(msg):
    text = f"""Ok, você gostaria de preparar algo doce ou salgado? (Escolha uma opção):
/doce para escolher doce
/salgado para escolher salgado"""
    bot.reply_to(msg, text)


def salgado(msg):
    text = f"""E quanto tempo você tem para preparar essa receita? (Escolha uma opção):
/poucotempo para preparar algo rápido
/muitotempo para preparar algo mais demorado"""
    bot.reply_to(msg, text)


def poucotempo(msg):
    text = f"""Incrível {msg.from_user.first_name}, de acordo com as suas respostas, acho que você gostaria
    de preparar essa receita:
    https://receitas.globo.com/receitas-sadia/file-mignon-suino-facil-de-fazer.ghtml
    """
    bot.reply_to(msg, text)


bot.polling()
