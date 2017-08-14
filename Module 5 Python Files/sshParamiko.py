import paramiko
import time

HOST = "192.168.1.202"
USER = "cisco"
PASS = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST,username=USER,password=PASS)

ssh_connection = ssh_client.invoke_shell()

ssh_connection.send("enable\n")
ssh_connection.send("cisco\n")
ssh_connection.send("conf t\n")

for vlan in range (10,51,10):
	ssh_connection.send("vlan " + str(vlan) + "\n")
	ssh_connection.send("name Paramiko_VLAN_" + str(vlan) + "\n")
ssh_connection.send("end\n")

time.sleep(1)

output = ssh_connection.recv(11111).decode(encoding="utf-8")

print(output)

ssh_client.close
