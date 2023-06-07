my_stack = list()
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())

class Stack:
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
    
my_stack2 = Stack()
my_stack2.push(1)
my_stack2.push(2)
my_stack2.push(3)
print(my_stack2)
print(my_stack2.pop())
print(my_stack2.peek())
print(my_stack2.pop())
print(my_stack2.pop())
print(my_stack2.pop())