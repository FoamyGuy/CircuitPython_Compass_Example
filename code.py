import time
import board
import busio
import adafruit_lis3mdl
from math import atan2, degrees

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

def vector_2_degrees(x, y):
    radians = atan2(y, x)
    degrees_calc = degrees(radians)
    if degrees_calc < 0:
        degrees_calc = 360 + degrees_calc
    return degrees_calc

def get_heading(sensor):
    magnet_axis_data = sensor.magnetic
    return vector_2_degrees(magnet_axis_data[0], magnet_axis_data[1])

while True:
    print("heading: %s" % get_heading(sensor))
    time.sleep(0.2)