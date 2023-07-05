import requests
import netmiko
import json

from netmiko import ConnectHandler
CSR1000v = { 
    "ip": "192.168.56.102",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",

}

connection = ConnectHandler(**CSR1000v)

output = connection.send_command('show ip interface brief')
print(output)

output = connection.send_command('show running-config')
print(output)

output = connection.send_command('show version')
print(output)

connection.disconnect()