#!/usr/bin/env python

f = open("RS.txt", 'w')

li = 0
wl = ""

while li != 1:
    choice = raw_input("Type 153 to close. \n")
    choice = int(choice)
    if choice != 153:
        wl = raw_input("Enter line \n")
        f.write(wl)
        f.write("\n")
    elif choice == 153:
        li = 1
        f.close()



