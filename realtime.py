import time
import earthquake
starttime = input("Insert start time (yy-mm-dd)")
endtime = input("Insert end time (yy-mm-dd)")

try:
    while True:
        earthquake.earthquake(starttime,endtime)
        time.sleep(20)
except KeyboardInterrupt:
    print("\tExiting...\n")
    exit()
