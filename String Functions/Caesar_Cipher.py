# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:36:04 2018

@author: joshu
"""
# A - Z  -> 65 - 90
# a - z  -> 97 - 122
# ord(yourletter)
# chr(your_code)

# Receive the message to encrypt and the shift amount

def caesar_cipher():
    message = input("Enter the message you want to be encrypted: ")
    shift_amount = eval(input("Enter the amount you want the characters shifted: "))
    secret = ''
    try:
        if message.isalpha():
            message_list = message.split()
        else:
            message_list = message.split(' ')
            
        for char in message_list:
            for i in char:
                secret += str((ord(i) + shift_amount))
                
            secret += ' '
        return secret
                
    except ValueError:
        print("The message contains an error ")

#print("The secret message is: ", caesar_cipher())
# Prepare the secret_message

# Cycle through each character in the message
    # Check if it isnt a letter keep it as it is
    
    
    
message = input("Enter your message: ")
key = int(input("How many characters should we shift: (1-26) "))

secret_message = ''

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
                
            if char_code < ord('A'):
                char_code += 26
                
        else:
            if char_code > ord('z'):
                char_code -= 26
                
            if char_code < ord('a'):
                char_code += 26
                
        secret_message += chr(char_code)
        
    else:
        secret_message += char
    
print("Encrypted : ", secret_message)
    
key = -key
    
original_massage = ''

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
                
            if char_code < ord('A'):
                char_code += 26
                
        else:
            if char_code > ord('z'):
                char_code -= 26
                
            if char_code < ord('a'):
                char_code += 26
                
        original_massage += chr(char_code)
        
    else:
        original_massage += char
    
print("Decrypted : ", original_massage)
        
        
        
