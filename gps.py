import time
import board
import adafruit_gps
import serial

def gps():
        uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
        gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
        gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        gps.send_command(b"PMTK220,1000")


        while True:
                gps.update()
                if not gps.has_fix:
                    # Try again if we don't have a fix yet.
                    print("Waiting for fix...")
                    continue
        gps = str({"Lat":gps.latitude,"Long":gps.longitude})
        return (gps)
if __name__== '__main__':
        gps()

        
