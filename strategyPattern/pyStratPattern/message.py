# class that holds the message uses to encrypt/decrypt
class Message:

    
    def __init__(self, message, strategy):
        self.message = message
        self.strategy = strategy

    #confirm I can access strategy class
    def getStrat(self):
        return self.strategy.toString()


