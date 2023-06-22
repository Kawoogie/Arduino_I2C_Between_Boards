import serial
import time

# make sure the 'COM#' is set according the Windows Device Manager
#  at the correct baud rate. The most common: 115200, 9600
ser = serial.Serial('COM8', 9600, timeout=1)
# Clear the serial output before starting data transmission
ser.flushInput()
# Give time for the serial connection to initialize
time.sleep(2)

while True:
    try:
        line = ser.readline().strip().decode()  # read a byte string
        print(line)
    except:
        print("Keyboard Interrupt")
        break

# End the serial connection
ser.close()

print("Done Taking Data")
