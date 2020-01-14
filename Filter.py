from datetime import datetime
unwanted = "410"
#unwanted2 = "-1"
#startdate = input("ANFANG:")
#enddate= input("ENDE:")
Raum = input("Raum: ")
times = open("timetable.txt","r")
writepointer = 0
inputDoc = open("YOURDIRECTORYINPUT" + str(Raum)+ ".csv","r")
data = inputDoc.readlines()
boundaries = times.readlines()
length = len(boundaries)
doclength = len(data)
for i in range(0,length,2):
	starttime = str(boundaries[i]).rstrip("\n")
	endtime = str(boundaries[i+1]).rstrip("\n")
	starttime_object = datetime.strptime(starttime, '%H:%M')
	endtime_object = datetime.strptime(endtime, '%H:%M')
	out = open("YOURDIRECTORYOUT"+ str(Raum)+"/" + str(int(((i+1)/2)+0.5))+". Stunde"+".csv","w+")
	out.write(data[0])
	for x in range(1,doclength-1,1):
		print(x)
		singleLine = data[x]
		checkvar_object = datetime.strptime(singleLine[11:16],'%H:%M')
		if checkvar_object<endtime_object and checkvar_object>starttime_object:
			writepointer = 1
			print("write")
		if unwanted in singleLine:
			writepointertemp = 0
		else:
			writepointertemp = 1
		if writepointer == 1 and writepointertemp ==1:
			out.write(str(singleLine))
		if checkvar_object>endtime_object or checkvar_object<starttime_object:
			if writepointer == 1:
				out.write(5*"\n")
			writepointer = 0
	out.close()
