from QuizzBot import QuizzBot
from Pg_manager import Pg_manager

from time import sleep, localtime, strftime
from colorama import Fore, Back, Style, init
import random, os, sys



init()

def time():
    return strftime("%d/%m/%Y %H:%M:%S", localtime())

id_quizz = "xari_le_fast"
pw_quizz = "Ka84(2r!G"

q = ""
a = ""

nbrQ = 0
nbrGoodAnswer = 0

bdd = Pg_manager("localhost", "squizz", "postgres", "admin", "5432")

bot = QuizzBot()

bot.connect_to_VPN()
print("connected to the VPN")

bot.connct_to_SQUIZ()
print("Connected to SQUIZZ")

#bot.connect_to_twitch(id_quizz, pw_quizz)
#print("connected to twitch")
#sleep(2)

bot.connect_to_initie()
print("connected to the room inite")

while(True):

    if nbrQ == 15:
        print(time() + "-> End of the game good answer  : " + Fore.GREEN + str(nbrGoodAnswer) + Style.RESET_ALL)
        nbrQ = 0
        nbrGoodAnswer = 0

    q = bot.scrapping_questions()
    answerQ = bdd.selectInitie(str(q))

    if answerQ == None:
        a = bot.scrapping_answers()
        bdd.insertInitie(str(q), str(a))

        print(time() + " -> Question added : " + q)
        print(time() + " -> Answer added : " + a)

        print(time() + Back.RED + Fore.WHITE + " -> No answered" + Style.RESET_ALL)
        bdd.insertReplyofBot("0")

        sleep(7.5)

    else:
        waiting = random.uniform(0, 3)
        print(time() + " -> Attente avant de répondre : " + str(waiting))
        sleep(waiting)

        answerSplit = "".join(answerQ).split(",")

        if len(answerSplit) == 1:
            answer = answerSplit[0].lower()
        elif len(answerSplit) == 2:
            answer =  answerSplit[random.randint(0, 1)].lower()
        elif len(answerSplit) > 2:
            answer = answerSplit[random.randint(0, 2)].lower()       

        bot.write_answer(answer.replace("l'", "").replace("un", "").replace("une", "").replace("le", "").replace("la", "").replace("les", ""))
        
        print(time() + " -> Question answered : " + q)
        print(time() + Back.GREEN + Fore.WHITE + " -> Answer writed : " + answer + Style.RESET_ALL)
        bdd.insertReplyofBot("1", str(q), str(answer))

        nbrGoodAnswer += 1

        sleep(18-waiting)

    nbrQ += 1


    






############################################
#id quizz = "xari_le_fast"
#pw quizz = "Ka84(2r!G"

# id gmail = xarilefast@gmail.com
# pw gmail = (F75qH6*t
############################################