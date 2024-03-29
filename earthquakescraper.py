import argparse
import os

import format
import scraper

parser = argparse.ArgumentParser()

''' Richiedi gli argomenti startDate ed EndDate come obbligatori'''

parser.add_argument("startDate")
parser.add_argument("endDate")
parser.add_argument("-v", "--verbose",
                    help="aumenta la verbosità dell'output", action="store_true")
parser.add_argument(
    "-p", "--place", help="Find earthquakes in a certain place")

args = parser.parse_args()
''' Crea un oggetto formattatore e uno scraper e passa a quest'ultimo data di inizio e fine, argomenti del file main'''
f = format.Formatter()

'''Flag verbosità'''

if args.verbose:
    f.verbosity = True


'''Se non è specificato un luogo, stampa tutta la lista'''


if args.place == None:
    data = scraper.get_earthquakes(args.startDate, args.endDate)
    w = open("out.txt", "w+", encoding="utf-8").writelines(data)
    x = f.format().to_string(index=False, header=False)
    print(x)



elif args.place != None:
    data = scraper.get_earthquakes(args.startDate, args.endDate)
    f.place = args.place
    w = open("out.txt", "w+", encoding="utf-8").writelines(data)
    x = f.format().to_string(index=False, header=False)
    print(x)

os.remove("out.txt")