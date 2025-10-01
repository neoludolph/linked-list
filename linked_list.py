class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_last(self, data):
        current = self.head
        node = Node(data)
        if current == None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

    def delete_node(self, index):
        current = self.head
        prev = None
        i = 0
        if index == 0:
            self.head = self.head.next
        elif index > 0:
            while i < index:
                prev = current
                current = current.next
                i += 1
            prev.next = current.next
        elif self.head == None:
            print("No node in list!")
        while 
            

    def print_list(self):
        current = self.head
        print("head -> ", end="")
        while current != None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print(None)
        
        
ll = LinkedList()

ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.delete_node(2)

ll.print_list()