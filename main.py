import argparse

import format
import scraper

parser = argparse.ArgumentParser()

''' Richiedi gli argomenti startDate ed EndDate come obbligatori'''

parser.add_argument("startDate")
parser.add_argument("endDate")
parser.add_argument("-v", "--verbose",
                    help="aumenta la verbosità dell'output", action="store_true")
parser.add_argument("-p", "--place", help="Find earthquakes in a certain place")

args = parser.parse_args()
''' Crea un oggetto formattatore e uno scraper e passa a quest'ultimo data di inizio e fine, argomenti del file main'''

f = format.Formatter()
x = scraper.Scraper(args.startDate, args.endDate)

'''Flag verbosità'''

if args.verbose:
    x.verbosityOn = True

else:
    pass

'''Se non è specificato un luogo, stampa tutta la lista'''
if args.place == None:

    w = open("file.txt", "w+").writelines(x.get_all_earthquakes())
    print(f.format().to_string(index=False, header=False))



else:
    print(args.place)
