import time
import board
import busio
from math import atan2, degrees

i2c = busio.I2C(board.SCL, board.SDA)

# Uncomment the import and initializer for your accelerometer.

#import adafruit_lis3dh
#sensor = adafruit_lis3dh.LIS3DH_I2C(i2c)

#import adafruit_lsm303_accel
#sensor = adafruit_lsm303_accel.LSM303_Accel(i2c)

import adafruit_mpu6050
sensor = adafruit_mpu6050.MPU6050(i2c)

def vector_2_degrees(x, y):
    radians = atan2(y, x)
    degrees_calc = degrees(radians)
    if degrees_calc < 0:
        degrees_calc = 360 + degrees_calc
    return degrees_calc


def get_inclination(sensor):
    return get_inclination_respect_x(sensor), get_inclination_respect_y(sensor)

def get_inclination_respect_x(sensor):
    accel_axis_data = get_data(sensor)
    vector_2_degrees(accel_axis_data[0], accel_axis_data[2])

def get_inclination_respect_y(sensor):
    accel_axis_data = get_data(sensor)
    return vector_2_degrees(accel_axis_data[1], accel_axis_data[2])

def get_data(sensor):
    return sensor.acceleration


while True:
    print("inclination: (%s, %s)" % (get_inclination(sensor)))
    time.sleep(0.2)

