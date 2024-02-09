stock_prices = {}

with open("stock_prices.csv", "r") as file:
    for line in file:
        tokens = line.split(', ')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices)

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
            return h % self.MAX
        
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
            

t = HashTable()
# t.add('march 12', 562)
t['march 13'] = 577
del t['march 13']
print(t.arr)
# print(t.get('march 12'))
print(t['march 13'])
