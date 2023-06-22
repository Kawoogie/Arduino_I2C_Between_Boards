import serial
import time
from datetime import datetime

# Set the file name with the date and time
file_name = "Data_" + str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".csv"

print("Creating File: ", file_name)

# open the file to save the output to
f = open(file_name, "w+")

# make sure the 'COM#' is set according the Windows Device Manager
#  at the correct baud rate. The most common: 115200, 9600
ser = serial.Serial('COM9', 115200, timeout=1)
# Clear the serial output before beginning
ser.flushInput()
# Give the serial connection time to initialize
time.sleep(2)

# How many data points to collect
data_points = 20000

# Wait for the data header before recording data
header = True
header_text = "X,Y,Z"

# Record the header data
while header:
    line = ser.readline().strip().decode("utf-8")
    if line == header_text:
        f.write(line + "\n")
        print(line)
        header = False

# Start recording the data stream
for _ in range(data_points):
    # Read a line from the serial port
    line = ser.readline().strip().decode("utf-8")
    if line:
        f.write(line + "\n")
        print(line)

# Close the file after taking data
f.close()
