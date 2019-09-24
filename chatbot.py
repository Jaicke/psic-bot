import telepot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Psic")
trainer = ListTrainer(bot)
train_list = open("train.txt", "r").readlines()
trainer.train(train_list)

token_api = os.getenv('TOKEN_TELEGRAM')

def toReceive(message):
  text = message['text']
  _id = message['from']['id']
  name = message['from']['first_name']
  response = bot.get_response(text)
  
  if 'Olá' in text or 'Oi' in text or 'start' in text:
    tele.sendMessage(_id, "Olá, {}.\nEu sou a Dra. Psic, minha especialidade é Ansiedade e Depressão.\nComo posso ajudar?".format(str(name)))
  elif response.confidence > 0.5:
    tele.sendMessage(_id, str(response))
  else:
    tele.sendMessage(_id, "Desculpa, não entendi.")

tele = telepot.Bot(token_api)
tele.message_loop(toReceive)

while True:
  pass