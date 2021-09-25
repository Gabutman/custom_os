from tqdm import tqdm
import socket,os,sys,time,random,psutil,datetime,schedule,multiprocessing

module =["pip","tqdm"]

ps = psutil.Process(os.getpid())

def warning(limit_ram=50,limit_disk=70,limit_swap=70,limit_cpu=50,energy_min=30):
	ram = psutil.virtual_memory()
	if ram.percent > limit_ram:
		print("[announcement]:watning ram utilization:"+str(ram.percent)+"%")
	disk = psutil.disk_usage("/")
	if disk.percent > limit_disk:
		print("[announcement]:warning storage utilization:"+str(disk.percent)+"%")
	swap = psutil.swap_memory()
	if swap.percent > limit_swap:
		print("[announcement]:warning swap memory utilization:"+str(swap.percent)+"%")
	cpu = psutil.cpu_percent(interval=1)
	if cpu.percent > limit_cpu:
		print("[announcement]:warning cpu usage:"+str(cpu.percent)+"%")
	battery = psutil.sensors_battery()
	if battery.percent < energy_min and not battery.power_plugged:
		print("[announcement]:warning energy remaining:"+str(battery.percent)+"%")
		
def schedule_func():
	schedule.every(1).second.do(warning)
	while True:
		schedule.run_pending()

def auto():
	while True:
		multiprocessing.Process(target=schedule_func,args=()).start()
		time.sleep(1)

def update():
	for i in module:
		os.system("pip install {} --upgrade".format(i))

def main():
	#multiprocessing.Process(target=auto,args=()).start()
	while True:
		command = input("$")
		cmd = ["ip","getip","help","update","now"]
		if command == cmd[0]:
			print("ip:",socket.gethostbyname(socket.gethostname()))
		elif command.find(cmd[1]) > -1:
			print("ip:",socket.gethostbyname(command.replace("get_ip","").replace(" ","")))
		elif command == cmd[2]:
			print(cmd)
			print(os.popen(command).read())
		elif command == cmd[3]:
			update()
		elif command == cmd[4]:
			print("now:",datetime.datetime.now())
		else:
			print(os.popen(command).read())
if __name__ == "__main__":
	main()
else:
	for i in tqdm(range(100)):
				time.sleep(random.uniform(0,3600))
	while True:
		while True:
			print("sh: {}: not found".format(input("$")))
