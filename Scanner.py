#!/usr/bin/python3

import nmap

#######################################
# Simple Port Scanner In Python
# -----------------------------
# Scans ports 1 - 1024 with user given
# ip address.
#
# By: Harman Rai
#######################################

#Creates new nmap scanner
scanner = nmap.PortScanner()

#Prints which version of nmap the user has
print(scanner.nmap_version())

print("This is a simple NMAP tool coded in Python")
print("<-------------------------------------------->")

#Gets user defined ip address to scan
ip_addr = input("Enter an IP address you want to scan: ")
print("You entered:",str(ip_addr))
scanner.scan(str(ip_addr),'1-1024','-v')
#print(scanner.scaninfo())
#print(scanner.csv())

print(scanner.scanstats())
print(scanner.all_hosts())
print(scanner[str(ip_addr)].state())
print(scanner[str(ip_addr)].all_protocols())
print(scanner[str(ip_addr)]['tcp'].keys())
print(scanner[str(ip_addr)].has_tcp(80))
