import socket
from _global import *

class TCPClient:
    def __init__(self, ipaddress, port) -> None:
        
        self.ipaddress = ipaddress
        self.port = port
        
        self.srvaddress = (self.ipaddress, self.port)
        self.tcpclient = None
    
    def TCPClientMain(self):
        self.tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while True:
            try:
                self.tcpclient.connect(self.srvaddress)
            except Exception as ex:
                print(f"{ex}")
                break
            
            self.tcpclient.send(controllercli.encode())
            recvidentif = self.tcpclient.recv(4096)
            
            if recvidentif == "valid":
                print("Client-Server versioning the same")
                
                while True:
                    print("Input IP address of specific server to power on/off")
                    ipcmd = input()
                
                    print("Input control command for server")
                    execcmd = input()
                
                    if execcmd != 0|1:
                        print("Please enter valid command")
                        break
                
                    else:
                        self.tcpclient.send(f"{ipcmd}/{execcmd}")
                
                
            elif recvidentif == "invalid":
                print("Disconnecting from server")
                print(f"Current controller version: {controllercli}")
                print("client-server versioning mismatch please update, ensure server and client are on the same version")
                self.tcpclient.close()
                break
                
                
            
            
                
                
                