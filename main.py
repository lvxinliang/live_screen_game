import serial
import time

def burst_balloon():
    ser.write(b'G1 Y0 F6000\n')
    ser.write(b'G1 Y-10 F6000\n')
    ser.write(b'G1 Y0 F6000\n')

def main_loop():
    burst_balloon()
    time.sleep(1)

    burst_balloon()
    time.sleep(1)

    burst_balloon()
    time.sleep(1)

if __name__ == '__main__':
    # Open the serial port
    ser = serial.Serial('COM4', baudrate=9600)

    # Check if the port is open
    if ser.is_open:
        print('Serial port is open')
        main_loop()

    else:
        print('Failed to open serial port')
        # Write the string to the serial port