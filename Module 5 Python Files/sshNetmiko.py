from netmiko import ConnectHandler

cat2960 = {
	"device_type": "cisco_ios",
	"ip": "192.168.1.202",
	"username": "cisco",
	"password": "cisco",
	"secret": "cisco",
}

net_connect = ConnectHandler(**cat2960)

net_connect.enable()

output = net_connect.send_command("show vlan brief")
print (output)

for vlan in range (10,51,10):
	config_commands = ["vlan " + str(vlan), "name Netmiko_VLAN_" + str(vlan)]
	output = net_connect.send_config_set(config_commands)
	print (output)

output = net_connect.send_command("show vlan brief")
print (output)
