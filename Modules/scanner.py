import socket
from Core.colors import *

class Scanners :

    def __init__(self, Host='', port='5555'):

        self.Host = Host

    def scan_port(self):

        for Xports in range(5555):

            S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            Connect = S.connect_ex((self.Host, Xports))

            if Connect == 0 :
                print(f'[{Green}+{White}] Open ---> 5555 ')
                break

            else:
                print(f'[{Red}-{White}] Close ---> 5555')
                break
              