import socket



def scan_range():
    
    ip = ["127.0.0.1","192.168.0.1"]
    for i in ip :
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((i,port))
            if 0 == result:
                print("Port: {} Open".format(port))
            sock.close()
        
scan_range()