import sys, socket
from datetime import datetime

#defining target
if len(sys.argv) == 2:  #sys.argv takes 2 input and is stored as array, [0] is the filename, [1] is the input provided
    target=socket.gethostbyname(sys.argv[1])  #translating hostname to ipv4
else:
    print("Invalid Syntax")


#banner
print("*" * 50)
print("*" * 50)
print("Scanning Target " +target)
print("Time started " +str(datetime.now()))
print("*" * 50)
print("*" * 50)

try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("scanning port {}".format(port))
        socket.setdefaulttimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0 :
            print("port " +str(port)+ " is open")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved")
    sys.exit()

except socket.error:
    print("COuldn't connnect to server")
    sys.exit()