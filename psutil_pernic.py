import psutil

network_stats = psutil.net_io_counters(pernic=True)#
bytes_sent = getattr(network_stats, 'bytes_sent')
bytes_recv = getattr(network_stats, 'bytes_recv')

print("Bytes Sent = {0} | Bytes Recived = {1}". format(bytes_sent, bytes_recv))
