class BinaryNodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryNodeTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryNodeTree(data)
                

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        
        return elements


    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.right
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

            # Alternative soultion
            # max_value = self.left.find_max()
            # self.data = max_value
            # self.left = self.left.delete(max_value)

        return self
    
def build_tree(elements):
    root = BinaryNodeTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [14, 5, 63, 76, 876, 34, 465, 765]
numbers_tree = build_tree(numbers)
print(numbers_tree.in_order_traversal())
numbers_tree.delete(76)
print(numbers_tree.pre_order_traversal())
print(numbers_tree.post_order_traversal())
print(numbers_tree.search(5))
print(numbers_tree.calculate_sum())
print(numbers_tree.find_max())
print(numbers_tree.find_min())
