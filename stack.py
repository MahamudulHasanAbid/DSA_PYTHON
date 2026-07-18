# STACK = LIFO(Last In First Out)

# Using a python list as a stack:
stack = []

# push
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")
print("Stack:", stack)

# pop
poped_elem = stack.pop()
print("Pop:", poped_elem )
print(stack)

# peek
top_elem = stack[-1]
print(top_elem)

# size
print("Size of the stack:", len(stack))

# isEmpty
isempty = not bool(stack)
print("isEmpty: ", isempty)

print(bool(stack))

# Using dedicated class. (Provide better encapsulation and additional functionality)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

print(stack.stack)
print("isEmpty: ", stack.isEmpty())
print("Size of the stack: ", stack.size())
print("Peek: ", stack.peek())
print("Pop element:", stack.pop())
