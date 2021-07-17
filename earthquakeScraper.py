import argparse
import scraper


parser = argparse.ArgumentParser()


''' Richiedi gli argomenti startDate ed EndDate come obbligatori'''

parser.add_argument("startDate")
parser.add_argument("endDate")
parser.add_argument("-v", "--verbosity",
                    help="aumenta la verbosità dell'output", action="store_true")
parser.add_argument("-p","--place",help="Find earthquakes in a certain place")


args = parser.parse_args()

if args.verbosity:
    x.verbosityOn = True


else:
    pass


x = scraper.Scraper(args.startDate,args.endDate)
    
