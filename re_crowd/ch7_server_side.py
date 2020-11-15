import socket as sk

b = open('1243.bin', 'rb').read()

ip = "0.0.0.0"
port = 4444

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

s.bind((ip, port))

s.listen(5)
sender = None
while True:
    client, addr = s.accept()
    sender = addr[0]
    print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))
    client.send(b)
    print("[+] Sent {0} bytes back".format(len(b)))
    client.close()
s.close()
print("DONE")
