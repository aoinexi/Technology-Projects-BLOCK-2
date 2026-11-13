# Read the Raspberry Pi temperature

## Temperature from the terminal

Here, we are using the Pi as if it was a temomether. To do so, let's track its temperature. Open a terminal and type:

```bash
vcgencmd measure_temp
```

Submit an image with the 
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/59466790-3e77-41ba-8d6d-cb5eda49c80b" />


## Do the same in python

Now, create a Python file with the following content :

```python
import subprocess

def read_temp():
    output = subprocess.check_output(["vcgencmd", "measure_temp"])
    temp_str = output.decode()  # e.g., "temp=47.8'C"
    temp_value = float(temp_str.replace("temp=", "").replace("'C", ""))
    return temp_value

if __name__ == "__main__":
    print("Temperature:", read_temp())
```

and run it in a terminal:

```bash
python3 read_temp.py
```

