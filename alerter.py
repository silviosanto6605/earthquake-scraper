import os
import subprocess

messaggio = open("terremotifiltrato.txt","r")
lettura = messaggio.readlines()

os.system("telegram-send "+str(lettura))