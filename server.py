import socket
from Crypto.Cipher import AES

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print "Got connection from ", addr
    c.send("Thank You for connecting")
    ciphertext = c.recv(1024)
    print "Message recieved !", ciphertext
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    decoded = obj2.decrypt(ciphertext)
    print "This is the decoded string !", decoded
    c.close()
