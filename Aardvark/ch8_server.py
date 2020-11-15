import socket as sock
import subprocess as sp

SOCK_PATH = "496b9b4b.ed5"
BACKLOG = 5
BUFF_SIZE = 10

def str_to_board(s: str):
    row1 = s[0:3]
    row2 = s[3:6]
    row3 = s[6:9]
    return [row1, row2, row3]

sp.run(['rm', SOCK_PATH], check=False)

sfd = sock.socket(sock.AF_UNIX, sock.SOCK_STREAM)
sfd.bind(SOCK_PATH)
sfd.listen(BACKLOG)
print("[*] listening...")
while True:
    print("[*] waiting for a connection...")
    cfd, addr = sfd.accept()
    print("[+] accepted connection")
    while True:
        recv_board = cfd.recv(BUFF_SIZE)
        recv_board = str(recv_board.decode("ascii"))
        if "wins!" in recv_board:
            print(recv_board)
            break
        for r in str_to_board(recv_board):
            print("\"{0}\"".format(r))
        row = int(input("[*] Enter row: ")) - 1
        col = int(input("[*] Enter column: ")) - 1
        move = bytes([ row, col ])
        cfd.send(move)
    cfd.close()
    print("[+] closed connection")
    break
sfd.close()
