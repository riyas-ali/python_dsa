from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.appendleft(item)

    def dequeue(self):
        if len(self.buffer) == 0:
            print('Queue is empty')
            return
        return self.buffer.pop()


food_items = [
    "Pizza",
    "Burger",
    "Pasta",
    "Salad",
    "Sushi",
    "Tacos",
    "Chicken Wings",
    "Ice Cream",
    "Chocolate Cake",
    "Fried Rice",
    "Steak",
    "Shrimp Scampi",
    "Cheese Sandwich",
    "Lasagna",
    "Fruit Salad"
]

q = Queue()
def add_order():
    for food in food_items:
        q.enqueue(food)
        print("Placing order for:",food)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while True:
        order = q.dequeue()
        if order is None:
            break
        else:
            print("Now serving: ",order)
            time.sleep(2)


t1 = threading.Thread(target=add_order)
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()
