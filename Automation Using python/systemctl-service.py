import subprocess

def manage_service(service_name,action):
	try:
		subprocess.run(['sudo','systemctl',action,service_name], check =True)
		print(f"Srvice {service_name} {action}ed successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Failed with exit code {e.returncode}")

if __name__=="__main__":
	manage_service('docker','start')