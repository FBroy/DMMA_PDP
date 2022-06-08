import scapy
from scapy.all import *	
import time


def sendPacket(src_ip, dst_ip):
	start = time.time()
	SYN = Ether(src="08:00:00:00:03:33", dst="08:00:00:00:01:11")/IP(dst=dst_ip,src=src_ip)/TCP(dport=1234, sport=50051, flags="S")
	# print(SYN.show())
	# MAKE SURE THE SERVER LISTENS ON PORT 1234!!
	SYNACK = srp1(SYN, iface="eth0")
	# print(SYNACK.show())
	end = time.time()

	# print(SYNACK.show())
	# print(SYNACK[TCP].flags)
	# if str(SYNACK[TCP].flags):
	# 	ACK = Ether(src="08:00:00:00:03:33", dst="08:00:00:00:01:11")/IP(dst=dst_ip,src=src_ip)/TCP(dport=1234, sport=50051, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)
	# 	sendp(ACK)

	# # terminate connection
	# FIN = Ether(src="08:00:00:00:03:33", dst="08:00:00:00:01:11")/IP(dst=dst_ip,src=src_ip)/TCP(sport=1234, dport=50051, flags="F", seq=SYNACK.ack, ack=SYNACK.seq + 1)
	# FINACK = srp1(FIN)
	# LASTACK = Ether(src="08:00:00:00:03:33", dst="08:00:00:00:01:11")/IP(dst=dst_ip,src=src_ip)/TCP(sport=1234, dport=50051, flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)
	# sendp(LASTACK)
	return end - start


response_times = []
counter = 1
while counter <= 100:
	print(counter)
	t = sendPacket("10.0.3.3", "10.0.1.1")
	response_times.append(t)
	counter += 1
	time.sleep(1)

f = open("results.txt", "w")
f.write('\n'.join(str(response_time) for response_time in response_times))
f.write("\nAverage: " + str(sum(response_times)/100))
f.close()