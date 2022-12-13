from TCPClient import *
from _global import *
from EventLogging import *

LoggingInit()
TCPClient(IPADDRESS, PORT).TCPClientMain()