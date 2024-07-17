#1. 1.	You are a Security Engineer at ACME company, and you are tasked to write a python code that will write the following Ip Addresses into a file named addresses.txt. (10.2.4.6, 10.10.160.23, 10.54.167.20)

f = open('addresses.txt','w')

f.write('10.2.4.6, ')
f.write('10.10.160.23, ')
f.write('10.54.167.20')

f = open("addresses.txt", "r")
print(f.read())

#2. You have been promoted to the senior pen-tester role at ACME company. You are currently tasked to create a number of wordlists called rockyou.txt that will be used to brute force an SSH account in order to get access to a remote target server. The words are PasswordADMIN, admin, abcd, and cows.
# Write code that will allow you to read rockyou.txt.


f = open('rockyou.txt','w')

f.write('PasswordADMIN, ')
f.write('admin, ')
f.write('abcd, ')
f.write('cows')

f = open("rockyou.txt", "r")
print(f.read())

#3. You currently work as a Help Desk Assistant and your boss has requested that you create code that will write different computer parts that are required to be replaced into a text file. The parts should be saved in a file called helpdesk.txt. The parts that are in need are New Keyboard, a New laptop screen, and five empty disks.

f = open('helpdesk.txt','w')

f.write('New keyboard, ')
f.write('New laptop screen, ')
f.write('five empty disks ')


f = open("helpdesk.txt", "r")
print(f.read())

#4.	Write a python code that writes any four devices that can be connected to your Wi-Fi into a file called devices.txt. 
#Write code that will allow you to read devices.txt.

f = open('devices.txt','w')

f.write('tv, ')
f.write('phone, ')
f.write('laptop ')


f = open("devices.txt", "r")
print(f.read())

#5.	Write a python code that writes your device MAC address into a text file called macaddress.txt. 

f = open('macaddress.txt','w')

f.write('MAC Address: MM:MM:MM:SS:SS:SS')

f = open("macaddress.txt", "r")
print(f.read())

