from netmiko import ConnectHandler  #importing netmiko

# entering the parameters of router for login
cisco_router = {
	'host': '192.168.126.137',
	'device_type': 'cisco_ios',
	'username': 'cisco',
	'password': 'cisco',
	'secret': 'cisco',
	}

output={}  # creating a empty dictionary for storing the output for future changes
connect = ConnectHandler(**cisco_router) #calling the parameter into the method and storing in variable

connect.enable() # this is to enter from usermode to privilege mode
output = connect.send_command ("show ip interface brief")

print output
