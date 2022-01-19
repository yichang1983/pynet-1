#!/usr/bin/env python
"""Read in the "show_arp.txt" file using the readlines() method. Use a list slice to
remove the header line.
Use pretty print to print out the resulting list to the screen, syntax is:
----
from pprint import pprint
pprint(some_var)
----
Use the list .sort() method to sort the list based on IP addresses.
Create a new list slice that is only the first three ARP entries.
Use the .join() method to join these first three arp entries back together as a single string
using the newline character ('\n') as the separator.
Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.readlines()

# Remove header line
show_arp = show_arp[1:]     #移除第一行月也就是從第一行開始讀取。
pprint(show_arp)            #用pprint 來印出。


show_arp.sort()
# Grab only the first four entries
my_entries = show_arp[:4]                 #：4 就是顯示0-3 個 list .
my_entries = "\n".join(my_entries)        #用"\n" 的意思下一行，也就是指 list 1和list 2在合併時用下一行來分開它們。

with open("arp_entries.txt", "wt") as f:    #打開 arp_entries.txt 並用wt 來寫入檔案，arp_entries.txt 簡稱為 f
    f.write(my_entries)                     #把第29行的執行結果用 f.write 來把它寫入。