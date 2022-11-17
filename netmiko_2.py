
# to represent the time and date taken  
from netmiko import ConnectHandler
 
#First create the device object using a dictionary
CSR = {
    "device_type": "cisco_ios",
	"ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
	
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
 
# Then send the command and print the output

#output_clock = net_connect.send_command('show clock')# send_command hold the netconnect
#output_clock = net_connect.send_command('show ip ro')
output_runconfig = net_connect.send_command('show runn')# active configuration 
print (output_runconfig)
 
# Finally close the connection
net_connect.disconnect() #if we don't disconnect the confige changes in the router will remain open while the remote connection -->on SSH/22 : MIM/MITM(man in middel/man in the middel)


#status of the router
#what are the ip's that the time interfaces are working with
#during the comm with the router 

#loop backe id's are also present as loopback<XXX>


