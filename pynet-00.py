import os, ipaddress

os.system('cls')
while True:   #infinite loop
	ip = input('Enter the IP Address')
	try:
		print(ipaddress.ip_address(ip))
		print('IP Vaild')
		
	except:
		print('-' *50)
		print('IP is not valid')
	finally:
		if ip =='q':
			print('Script Finish')
			break