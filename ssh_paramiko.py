
from netmiko import ConnectHandler  #importing netmiko
import getpass
import sys

ip = sys.argv[1]
user = sys.argv[2]

if len(sys.argv)<2:
	print "arguments missing\n"
	print "Format = <python ssh.py> <Host ip address> <username>"
	sys.exit(1)

else:
	#entering the parameters of router for login
	cisco_router = {
	     'host': ip,
	     'device_type': 'cisco_ios',
	     'username': user,
	     'password': getpass.getpass(),
	     'secret': 'cisco',
	     }

	output={}  # creating a empty dictionary for storing the output for future changes
	connect = ConnectHandler(**cisco_router) #calling the parameter into the method and storing in variable
	connect.enable() # this is to enter from usermode to privilege mode
	output = connect.send_command ("show ip interface brief")
	print ("{:>50}".format("This is Interface table\n"))
	print (output)
	
	connect.disconnect()



