#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import sys
def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        print "Connected to %s on port %s" % (address, port)
        return True
    except socket.error, e:
        print "Connection to %s on port %s failed: %s" % (address, port, e)
        return False
    finally:
        s.close()

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()

    #parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")

    #parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for server", metavar="PORT")
    parser.add_option("-f", "--filename", dest="filename", help="CSV file with list of addresses and ports", metavar="FILENAME")

    (options, args) = parser.parse_args()
    file = open(options.filename, "r")
    lines = file.readlines()
    for line in lines:

        address = line.split(',')[0]
        port = int(line.split(',')[1])

        check = check_server(address, port)
        print(line)
        print 'check_server returned %s' % check

    file.close()



    


    sys.exit(not check)