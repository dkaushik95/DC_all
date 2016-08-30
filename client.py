import socket
from Crypto.Cipher import AES

s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print s.recv(1024)
message = raw_input("Enter the message: ")
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
ciphertext = obj.encrypt(message)
print "Encoded message is ", ciphertext
print "Sending to server for decrypting"
s.send(ciphertext)

s.close()
