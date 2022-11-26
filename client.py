import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port= 8081
client.connect(('127.0.0.1', port))
response = client.recv(port)
name = input(response.decode())
client.send(str.encode(name))
response = client.recv(port)
password = input(response.decode())
client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''
response = client.recv(2048)
response = response.decode()

print(response)
client.close()