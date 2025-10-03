class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top.data
            self.top = self.top.next
            return popped_node
        
    def peek(self):
        if self.top is None:
            return None
        return self.top.data


    def print_stack(self):
        current = self.top
        print("top -> ", end="")
        while current != None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print(None)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
