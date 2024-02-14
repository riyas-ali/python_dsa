from collections import deque

class Stack:
    def __init__(self):
        self.cotainer = deque()

    def push(self, val):
        self.cotainer.append(val)

    def pop(self):
        return self.cotainer.pop()

    def peek(self):
        return self.cotainer[-1]
    
    def is_empty(self):
        return len(self.cotainer) == 0
    
    def size(self):
        return len(self.cotainer)
    
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


s = Stack()
s.push(3)
s.push(4)
s.push(6)
print(s.cotainer)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())
print(reverse_string("We will conquere COVI-19"))
