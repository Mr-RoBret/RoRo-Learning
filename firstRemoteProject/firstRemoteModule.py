'''
Created on Jan 10, 2018

@author: bretfarley
'''

class MyClass:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def sayHello(self, greeting):
        self.greeting = greeting
        msg = str(greeting)
        return msg
        
x = MyClass()
myGreeting = "Hello, Worlds!"
print(x.sayHello(myGreeting))



        