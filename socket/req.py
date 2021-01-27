
import socket

host_name = socket.gethostname()
print(host_name)

ipv4 = socket.gethostbyname(host_name)
print(ipv4)

port = 21

servise = socket.getservbyport(port , 'tcp')

print(servise)

print('#' * 50)

data  = 12345

long_data = socket.htonl(data)

short_data = socket.htons(data)

print(long_data)
print(short_data)