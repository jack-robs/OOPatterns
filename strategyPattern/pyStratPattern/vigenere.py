# class for vignere cipher
class Vig: 
    
    def __init__(self):
        self.name = "vigenere cipher"


    def encrypt(self, messageClass):
        '''
        Encrypts using class parameter: messageClass
        Called in message.py in encrypt()
        returns: string (for now, just to confirm method access)
        '''
        return "Vig encrypting: " + messageClass.getMessage()
        

    def toString(self):
        return 'Using Strategy: ' + self.name

