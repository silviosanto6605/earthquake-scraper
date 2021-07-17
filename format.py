# TODO: Scrivere parser per l'output del file principale
import pandas as pd

class Formatter():

    inp:str


    def __init__(self):
        self.inp = ""
        

    def format(self,inp):
        with open (inp) as f:
            for line in f:
                #f.write(line.split("|"))
                print(line)