#from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

#get the all network adapter MAC addresses
all_mac = {iface.mac for iface in ifaces.values()}
print(all_mac)
#A dictionary to map each connection to its corresponding
connection2pid = {}
#a dictionary to map each process ID (PID) to total Upload (0) and Download (1) traffic
pid2triffic = defaultdict(lambda: [0, 0])
print(pid2triffic)
#the glObal Pandas DataFrame that's used to track previous traffic stats
global_df = None

is_program_running = True

#function with  body is called as--> function declaration ,defination
def get_size(bytes):

	"""
	Returns size of bytes in a nice format
	"""
	for unit in ['', 'K', 'M', 'G', 'T', 'P']:  #binary Mnemonice
		if bytes < 1024:
			return f"{bytes:.2f}{unit}B" #rounding of the flow (.2f)
		bytes /= 1024
		
io =psutil.net_io_counters(pernic=True)

while True:
	
	time.sleep(UPDATE_DELAY)
	
	upload_speed, download_speed = io_2[iface].bytes_sent -iface_io.bytes_sent, io_2[iface].bytese_sent, io_2[iface].bytes_recv - iface_io.bytes_sent,
	
	data.append({
		"iface": iface, "Download": get_size(io_2[iface].bytes_recv),
		"Upload": get_size(io_2[iface].bytes_sent),
		"Upload Speed": f"{get_size(upload_speed/ UPDATE_DELAY)}/s",
		"Download Speed": f"{get_size(download_speed/ UPDATE_DELAY)}/s,		
		})
		
	io = io_2
	
	df =pd.Dataframe(data)
	
	df.sort_values("Download", inplace=True, ascending=False)
	
	os.system("cls") if "nt" in os.name else os.system("clear")
	
	print(df.to_string())