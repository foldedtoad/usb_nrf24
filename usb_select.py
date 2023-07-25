import serial
from serial.tools import list_ports

def port_selector():

	enmu_ports = enumerate(list_ports.comports())

	table_of_ports = []

	for n, (p, descriptor, hid) in enmu_ports:
		if "VID:PID=1A86:7523" in hid:
			table_of_ports.append(p)

	elements = len(table_of_ports)

	if elements == 0 :
		print("\nError: No suitable ports found\n")
		return None

	print("List of available devices")
	for n in table_of_ports:
		print("  " + str(table_of_ports.index(n)), str(n))

	while 1 :
		raw = input("Enter number for port to use: ")
		if raw.isdigit() :
			select = int(raw)
			if (select >= 0 and select < elements) :
				print("Selected " + table_of_ports[select])
				return table_of_ports[select]
		print("Error: Invalid selection...try again")

	pass

if __name__ == "__main__":
	port_selector()
