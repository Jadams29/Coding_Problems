# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:35:22 2018

@author: joshu
"""

# Enter a string to hide in uppercase : HIDE

# Secret Message : 35647890

# Original Message : HIDE


message =input("Enter a string to hide: ")
secret_message = ''

for i in range(len(message)):
    secret_message += str(ord(message[i]))
print("The secret message for {} is {}".format(message, secret_message))
print("Convert the secret message {} back into original message". format(secret_message))

# Using list comprehension

secret_Message_List = [ord(i) for i in message]
print("Using list comprehension the list is: ", secret_Message_List)
decypted_message = [chr(i) for i in secret_Message_List]
print("Using list comprehension to decrypt the message: ", decypted_message)



    
