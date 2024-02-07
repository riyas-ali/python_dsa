class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):

        if self.head is None:
            print(f"The list is empty.")
            return
        
        itr = self.head
        dllstr = ''

        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next

        print(dllstr)


    def print_backward(self):
        itr = self.head

        if itr is None:
            print(f"The list is empty.")
            return
        
        itr = self.get_last_node()
        dllstr = ''

        while itr:
            dllstr +=  str(itr.data)+'-->'
            itr = itr.prev
        
        print("Link list in reverse: ", dllstr)


    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next
        
        return itr

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):

        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node


    def insert_at_end(self, data):
        itr = self.head

        if itr is None:
            node = Node(data, None, None)
            self.head = node
            return
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        itr = self.head

        if itr is None:
            self.insert_at_end(data)

        count = 0
        
        while itr:
            if index < 0 or index > self.get_length():
                raise Exception('Invalid Index')

            if index == 0:
                self.insert_at_begining(data)

            if count == index -1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node

                itr.next = node
                break

            count += 1
            itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")
        
        itr = self.head
        count = 0

        if index == 0:
            itr = itr.next
            itr.prev = None
            return

        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            count += 1
            itr = itr.next

    def insert_values(self, data_list):

        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_begining('a')
    ll.insert_at_end('b')
    ll.insert_at_end('c')
    ll.insert_at_end('d')
    ll.insert_at_end('E')
    ll.insert_at(2,'x')
    ll.remove_at(3)
    ll.insert_values(['z', 'y','w','v'])
    print("Length of the list : ",ll.get_length())
    ll.print_forward()
    ll.print_backward()
