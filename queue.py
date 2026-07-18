# # Queue(FIFO= First in First out)

# # Queue using List
# queue = []

# # Enqueue
# queue.append("A")
# queue.append("B")
# queue.append("C")
# queue.append("D")
# queue.append("E")
# print(queue)

# # Peek
# peek = queue[0]
# print(peek)

# # Dequeue
# dequeue = queue.pop(0)
# print(queue)
# print("Poped Element: ",dequeue)

# # Size
# size = len(queue)
# print("Size: ",size)

# # isEmpty
# isempty = not bool(queue)
# print("isEmpty: ",isempty)

# Queue using class

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def peek(self):
        if self.isEmpty():
            return "There is nothing in the queue."
        return self.queue[0]
    
    def dequeue(self):
        if self.isEmpty():
            return " Queue is Empty."
        return self.queue.pop(0)
    
    def isEmpty(self):
        isempty = not bool(queue)
        return isempty
    def size(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.enqueue("d")
queue.enqueue("e")

print(queue.queue)

print("Dequeue: ", queue.dequeue())
print("Peeking: ", queue.peek())
print("IsEmpty: ", queue.isEmpty())
print("Size: ", queue.size())

print(queue.queue)
