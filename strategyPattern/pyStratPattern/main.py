from caesar import *
from message import *
from vigenere import *

'''
Project: strategy pattern impelemented in python
Context class: message.py, the text to be encrypted/decrypted 
Strategy classes:
* parent class - (TODO) encrypt.py, (generic encryption class) 
* child classes - caesar.py, vigenere.py (encryption algorithms)
'''


def main(): 
    '''
    1) take input from user of text to encrypt 
    2) take input from user of encryption type, plus other relevant details
    -> i.e.: caesar, ask for shift, vigenere, ask for keyword
    3) output cipher text and original
    '''
    userText = input("input text to encrypt> ")
    print("\nEnter '1' for caesar cipher\nEnter '2' for vigenere")
    cipherType = int(input("input cipher type> "))
    
    if cipherType == 1:
        print("Chose caesar cipher")
        strat = Caesar()
        message = Message(userText, strat)
        strat = message.getStrat()
        cipher = message.encrypt()
        print(strat)
        print(cipher)

    elif cipherType == 2:
        print("Chose vig cipher")
        # cipher = vig(....)
    else:
        print("no cipher chose")
        # while loop or exit

main()
