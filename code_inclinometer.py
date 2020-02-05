import time
import board
import busio
from math import atan2, degrees

i2c = busio.I2C(board.SCL, board.SDA)

# Uncomment the import and initializer for your accelerometer.

import adafruit_lsm303_accel
sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)

def vector_2_degrees(x, y):
    radians = atan2(y, x)
    degrees_calc = degrees(radians)
    if degrees_calc < 0:
        degrees_calc = 360 + degrees_calc
    return degrees_calc


def get_inclination(self):
    return self.get_inclination_respect_x(), self.get_inclination_respect_y()

def get_inclination_respect_x(self):
    accel_axis_data = get_data()
    vector_2_degrees(accel_axis_data[0], accel_axis_data[2])

def get_inclination_respect_y(sensor):
    accel_axis_data = get_data()
    return vector_2_degrees(accel_axis_data[1], accel_axis_data[2])

def get_data(sensor):
    return sensor.read_accelerometer()


while True:
    print("inclination: (%s, %s)" % (get_inclination(sensor)))
    time.sleep(0.2)

