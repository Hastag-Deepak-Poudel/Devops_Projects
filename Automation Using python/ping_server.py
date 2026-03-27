import subprocess

def ping_server(server):
	for server in servers:
		response = subprocess.call(["ping", "-c", "3", server])
		if response == 0:
			print(f"{server} is up!!")
		else:
			print(f"{server} is down!!")

servers = ["8.8.8.8","8.8.4.4","192.168.1.91","google.com","192.168.2.1"]
ping_server(servers)