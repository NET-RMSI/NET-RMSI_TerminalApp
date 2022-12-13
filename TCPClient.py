import socket
from _global import *
from EventLogging import *

class TCPClient:
    def __init__(self, ipaddress, port) -> None:
        
        self.ipaddress = ipaddress
        self.port = port
        
        self.srvaddress = (self.ipaddress, self.port)
        self.tcpclient = None
    
    def TCPClientMain(self):
        self.tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.tcpclient.connect(self.srvaddress)
        except Exception as ex:
            LOGEVENTS_ERROR(ex)                
            
        self.tcpclient.send(controllercli.encode())
        recvidentif = self.tcpclient.recv(4096).decode()
            
        if recvidentif == "valid":
            LOGEVENTS_INFO("Client-Server versioning the same")
                
            
                    
            ipcmd = input("Input IP address of specific server to power on/off")
                    
            execcmd = input("Input control command for server")
                
            
            
            self.tcpclient.send(f"{ipcmd}/{execcmd}".encode())
            
                
        elif recvidentif == "invalid":
            LOGEVENTS_INFO("Disconnecting from server")
            LOGEVENTS_INFO(f"Current controller version: {controllercli}")
            LOGEVENTS_INFO("client-server versioning mismatch please update, ensure server and client are on the same version")
            self.tcpclient.close()
                
                
                
            
            
                
                
                