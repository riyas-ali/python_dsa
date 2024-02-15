class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,  self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count  += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count  += 1

    def insert_after_value(self, data_after, data_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_insert, itr.next)
                return
            itr = itr.next

        print('%s is not present in linked list.' % str(data_after))
        self.insert_at_begining(data_insert)

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(78)
    ll.insert_at_end(65)
    ll.insert_at_end(12)
    ll.insert_values(['apple', 'banana', 'cherry', 'grape', 'mango'])
    ll.remove_at(2)
    ll.insert_at(0,"dates")
    ll.insert_at(3,"jackfruit")
    ll.insert_after_value('apple', "milk")
    ll.insert_after_value('cocunut', "coconut")
    ll.remove_by_value("grape")
    ll.print()
    print(f'Length of linked list : {ll.get_length()}')