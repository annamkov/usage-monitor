import psutil
import time

#\r (carriage return) resets the cursor position to the beginning of the line,
# which makes print statements periodically overwrite previous output.

# end="" sets the last character of print to be an empty string instead of the default \n.
# this keeps the output occuring on the same line

def show_usage(cpu_usage, bars=50):
    cpu_percent = (cpu_usage / 100.00)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    print(f"\rCPU Usage: |{cpu_bar}| |{cpu_usage}%|", end="")

while(True):
    show_usage(psutil.cpu_percent())
    time.sleep(0.50)
