import argparse
import format
import scraper


parser = argparse.ArgumentParser()


''' Richiedi gli argomenti startDate ed EndDate come obbligatori'''

parser.add_argument("startDate")
parser.add_argument("endDate")
parser.add_argument("-v", "--verbose",
                    help="aumenta la verbosità dell'output", action="store_true")
parser.add_argument("-p","--place",help="Find earthquakes in a certain place")


args = parser.parse_args()
f = format.Formatter()

x = scraper.Scraper(args.startDate,args.endDate)

if args.verbose:
    x.verbosityOn = True

else:
    pass

if args.place == None:

    w = open("file.txt","w+").writelines(x.get_all_earthquakes())
    f.format("file.txt")
    
    

else:
    print(args.place)

