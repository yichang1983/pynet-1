#!/usr/bin/env python
"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""
from __future__ import print_function, unicode_literals

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.read()

bgp_summ = bgp_summ.splitlines()
print(bgp_summ)                                       # this print is for testing actually no need.
print ("*****************************")               # this print is for testing actually no need.
first_line = bgp_summ[0]
print(first_line)                                     #this print is for testing actually no need.
print ("*****************************")               #this print is for testing actually no need.
as_number = first_line.split()[-1]
print("Local AS Number: {}".format(as_number))        #"{}.format() 是將as_number 傳進去｛｝裡。
last_line = bgp_summ[-1]
peer_ip = last_line.split()[0]
print("BGP Peer IP Address: {}".format(peer_ip))      #"{}.format() 是將peer_ip 傳進去｛｝裡。