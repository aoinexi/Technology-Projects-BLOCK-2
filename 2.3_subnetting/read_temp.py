import subprocess

def read_temp():
	output = subprocess.check_output(["vcgencmd", "measure_temp"])
	temp_str = output.decode() # e.g., "temp=47.8'C"
	temp_value = float(temp_str.replace("temp=", "").replace("'C", ""))
	return temp_value

if __name__ == "__main__":
	print("Temperature:", read_temp())
