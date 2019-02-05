from __future__ import print_function
import socket
import sys 



def main(path, ip,  port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

    s.connect((ip, port))

    s.sendall("GET {} HTTP/1.1\r\n\r\n".format(path))

    all_responses = [] 
    while True:
        chunk = s.recv(4096) 
        if chunk == b'':
            break 
        else:
            all_responses.append(chunk)

    print(''.join(all_responses))


if  __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except:
        print("Err. Usage: python client.py path ip port_no")