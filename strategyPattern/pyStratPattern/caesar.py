# class for caesar cipher 
class Caesar: 
    
    def __init__(self):
        self.name = "caesar cipher"


    def encrypt(self, messageClass):
        '''
        Encrypts using class parameter: messageClass
        Called in message.py in encrypt()
        returns: string (for now, just to confirm method access)
        '''
        #TODO actual encryption logic
        return "Caesar encrypting: " + messageClass.getMessage()
        

    def toString(self):
        return 'Using Strategy: ' + self.name

    

