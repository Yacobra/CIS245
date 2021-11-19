
#Jacob Darling
#Assignment 10.1
#Create a program that allows a user to specify a directory to save a file containing their input (name, address, number)
import os

#Collect user input
dir_input = input("Please choose the directory where you would like to save the file: ")
file_name = input("Please enter name of file: ")
name = input("Enter your name: ")
address = input("Enter your address: ")
phone_number = input("Enter your phone number: ")

#checks for directory
if os.path.isdir(dir_input):
    #Creates or overwrites file specified by user
    writeF = open(os.path.join(dir_input, file_name), 'w')
    writeF.write(name + ', ' + address + ', ' + phone_number)

    #Remember to close file
    writeF.close()

    print("File contents: ")
    readF = open(os.path.join(dir_input, file_name))

    #prints resulting comma separated list
    for line in readF:
        print(line)

    #Remember to close file
    readF.close()

else:
    print("Sorry that directory does not exist.")