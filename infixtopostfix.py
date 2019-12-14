'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
    def push(self, val):
        self.items.append(val)
        self.length += 1
        
    def pop(self):
        if self.empty():
            return null
        self.length -= 1
        return self.items.pop()
        
    def size(self):
        return self.length
    
    def peek(self):
        if self.empty():
            return null
        return self.items[0]
    
    def empty(self):
        return self.length == 0

        
priority = {}
priority['*'] = 2
priority['/'] = 2
priority['+'] = 1
priority['-'] = 1

        
def convert(expression):
    print(convert1(expression.split()))
    
def convert1(exp):
    postfix = []
    op = Stack()
    
    for i in exp:
        if i.isidentifier():
            postfix.append(i)
        else:
            if not op.empty():
                temp = op.peek()
            
                while not op.empty() and priority[temp] >= priority[i] and i.isidentifier():
                    postfix.append(op.pop())
                    temp = op.peek()
                
            op.push(i)
                
    while not op.empty():
        postfix.append(op.pop())
            
    return postfix
        
convert(input("Enter any Expression:\n"))   

