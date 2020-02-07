""" Display inclination data five times per second """
import time
from math import atan2, degrees
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

# Uncomment the import and initializer for your magnetometer.

# import adafruit_lis3mdl
# sensor = adafruit_lis3mdl.LIS3MDL(i2c)

import adafruit_lsm303dlh_mag
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, magnet_z = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)


while True:
    print("heading: {.2f}deg".format(get_heading(sensor)))
    time.sleep(0.2)
