#Importing the necessary modules
#netmiko is a multi-vendor SSH Python library that simplifies the process of connecting to network devices via SSH.
#This library adds vendor-specific logic to paramiko, which is the de-facto SSH library in Python.
import datetime
from netmiko import ConnectHandler


#Defining the device to monitor
ip = '10.10.10.2'

#Defining the device type for running netmiko
device_type = 'arista_eos'

#Defining the username and password for running netmiko
username = 'jaga'
password = 'reddy'

#Defining the command to send to each device
command = 'show running'


#Connecting to the device via SSH
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)

#Entering enable mode
enable = session.enable()

#Sending the command and storing the output (running configuration)
output = session.send_command(command)

#Writing the command output to a file with today.
with open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')
#End Of Program
