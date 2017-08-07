from threading import Thread
import os, re

class ip_check(Thread):
	def __init__(self, ip):
		Thread.__init__(self)
		self.ip = ip
		self.__successful_pings = -1

	def run(self):
		ping_out = os.popen('ping -q -c2 '+ self.ip, 'r')
		while True:
			line = ping_out.readline()
			if not line: break
			n_received = re.findall(received_packages, line)
			if n_received:
				self.__successful_pings = int(n_received[0])

	def status(self):
		if self.__successful_pings == 0:
			return 'No Response'
		if self.__successful_pings == 1:
			return 'Alive, but 50% packet loss'
		if self.__successful_pings == 2:
			return 'Alive'
		else:
			return 'Unknown Error'
received_packages = re.compile(r'(\d) received')
check_results = []

for suffix in range(1,256):
	ip = "10.1.6." + str(suffix)
	current = ip_check(ip)
	check_results.append(current)
	current.start()

for el in check_results:
	el.join()
	print 'IP : %s Stat: %s' % (el.ip, el.status())
