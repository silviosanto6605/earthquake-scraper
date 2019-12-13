import subprocess
import os

starttime = input("Insert start time (yy-mm-dd)")

endtime = input("Insert end time (yy-mm-dd)")


t = os.system('''curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime='''+starttime+'''T00:00:00&endtime='''+endtime+'''T22:22:00&format=text" > terremoti.txt''')
subprocess.call(["bash search.sh"],shell=True)
exit(0)