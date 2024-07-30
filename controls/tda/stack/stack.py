from controls.tda.stack.stackOperation import StackOperation
class Stack:
    def __init__(self, tope):
        self.__stack = StackOperation(tope)

    @property
    def _stack(self):
        return self.__stack

    @_stack.setter
    def _stack(self, value):
        self.__stack = value

    
    def push(self, data):
        self.__stack.push(data)
    
    def pop(self):
        return self.__stack.pop
    

    def print(self):
        self.__stack.print


    def verify(self):
        return self.__stack.verifyTop
    
    @property
    def clear(self):
        self.__stack.clear