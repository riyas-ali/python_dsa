from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, item):
        self.buffer.appendleft(item)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
pq = Queue()
pq.enqueue({
    'company': 'TCS',
    'timestamp': '15 Apr, 11.01 AM',
    'price': '234'
})
pq.enqueue({
    'company': 'TCS',
    'timestamp': '15 Apr, 11.02 AM',
    'price': '235'
})
pq.enqueue({
    'company': 'TCS',
    'timestamp': '15 Apr, 11.03 AM',
    'price': '236'
})

print(pq.buffer)
print(pq.dequeue())