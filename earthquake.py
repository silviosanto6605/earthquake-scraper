def earthquake(starttime,endtime):
	try:
		import subprocess
		import os
		t = os.system('''curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime='''+starttime+'''T00:00:00&endtime='''+endtime+'''T22:22:00&format=text" > terremoti.txt''')
		subprocess.call(["bash search.sh"],shell=True)
		os.system("python3 alerter.py")

	except KeyboardInterrupt:
		print("\tExiting...\n")
		exit()
