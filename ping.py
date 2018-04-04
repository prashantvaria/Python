import os

#i =0
#for i in range (0,3):
while True:
	a = raw_input("please enter the domain name or ip address you want to ping\n")
	print ("Your ip address is %s"%a)
	print("\n")
	ping = ("ping -c 10 "+a)
	os.system(ping)
	print("\n")

	cont = raw_input("Do you want to ping to other destination? yes/no ")
	while cont.lower() not in ("yes","no"):
		cont = raw_input ("Wrong input, Please choose either yes/no ")
	if cont =="no":
		break

	
