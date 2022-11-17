from netmiko import ConnectHandler

CSR = {
		"device_type": "cisco_ios",
		"ip": "sandbox-iosxe-latest-1.cisco.com",
		"username": "developer",
		"password": "C1sco12345"
		}

net_connect = ConnectHandler(**CSR)
	
#discover the hostname
hostname = net_connect.send_command("show run | i host")
#hostname = net_connect.send_command("show clock")
hostname.split(" ")
#hostname, device= hostname.split(" ")

hostname ,device, *rest = hostname.split(" ")# device that are connected to the host
# split the host name and device by using -->*rest

print("Backing up "+ device)

filename = "C:\\Users\\user410\\Desktop\\pythonfiles\\device3.txt"
#save bachup in same folder as script use below line and comment out above line
#filename = device + '.txt'

# showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a") #in append mode
# log_file.write(showrun)
# log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

#finally close the connection
net_connect.disconnect()