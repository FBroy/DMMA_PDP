import scapy
from scapy.all import *
import time


def sendPacket(src_ip, dst_ip, counter):
	packet = Ether(src="08:00:00:00:03:33", dst="08:00:00:00:01:11")/IP(dst=dst_ip,src=src_ip)/TCP(dport=1234, sport=52551)/("Are you there? " + str(counter))
	# packet.show()
	response = srp1(packet, iface="eth0")
	return response.time - packet.sent_time

response_times = []
counter = 1

while counter <= 100:
	print(counter)
	t = sendPacket("10.0.3.3", "10.0.1.1", counter)
	response_times.append(t)
	counter += 1
	time.sleep(1)

f = open("results.txt", "w")
f.write('\n'.join(str(response_time) for response_time in response_times))
f.write("\nAverage: " + str(sum(response_times)/100))
f.close()