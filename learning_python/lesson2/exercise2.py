#!/usr/bin/env python
"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""
from __future__ import print_function, unicode_literals

my_ipaddress = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4", "5.5.5.5"]
my_ipaddress.append("6.6.6.6")
my_ipaddress.extend(["7.7.7.7", "8.8.8.8"])
my_ipaddress = my_ipaddress + ["9.9.9.9", "10.10.10.10"]
print(my_ipaddress)

print(my_ipaddress[0])
print(my_ipaddress[-1])

first_ip = my_ipaddress.pop(0)
last_ip = my_ipaddress.pop()

my_ipaddress[0] = "99.99.99.99"
print(my_ipaddress[0])