import serial
import time
import subprocess
from ArduinoPy import Device

virtual_device = Device.Device() 
device_path = virtual_device.findDevice("linux")
device = virtual_device.getDevice(device_path[0])

subprocess_PIPE = subprocess.PIPE
speed = 0

def volume_up():
    subprocess.Popen(["amixer set 'Master' 5%+"], stdout = self.PIPE, shell=True).communicate()[0]

def volume_down():
    subprocess.Popen(["amixer set 'Master' 5%-"], stdout = self.PIPE, shell=True).communicate()[0]


while True:
    serial_value = virtual_device.readSerialOnce(device) 
    print serial_value.strip()

    #system volume up
    if serial_value.strip() == "unix_volume_up":
        print subprocess.Popen(["amixer set 'Master' 5%+"], stdout = subprocess_PIPE, shell=True).communicate()[0]

    #system volume down
    if serial_value.strip() == "unix_volume_down": 
        print subprocess.Popen(["amixer set 'Master' 5%-"], stdout = subprocess_PIPE, shell=True).communicate()[0]

    #vlc play/pause/normal(if speed=!0)
    if serial_value.strip() == "2011275475":
        if speed == 0:
            print subprocess.Popen(["echo -n  'pause' | nc -U ~/.vlc_socket"], stdout=subprocess_PIPE, shell=True).communicate()[0]
        else:
            print subprocess.Popen(["echo -n  'normal' | nc -U ~/.vlc_socket"], stdout=subprocess_PIPE, shell=True).communicate()[0]
            speed = 0
            

    #fast back -5 sec
    if serial_value.strip() == "2011271379":
        print subprocess.Popen(["echo -n  'rewind' | nc -U ~/.vlc_socket"], stdout=subprocess_PIPE, shell=True).communicate()
        speed = speed - 1

    #fast forw+
    if serial_value.strip() == "2011259091":
        print subprocess.Popen(["echo -n  'fastforward' | nc -U ~/.vlc_socket"], stdout=subprocess_PIPE, shell=True).communicate()[0]
        speed = speed + 1
