class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        data = self.head.data
        self.head = self.head.next
        print("Popped:", data)
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return
        data = self.head.data
        self.head = self.head.next
        print("Dequeued:", data)
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
linked_list = LinkedList()
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)
print("After Push:")
linked_list.display()
linked_list.pop()
print("After Pop:")
linked_list.display()
linked_list.enqueue(40)
linked_list.enqueue(50)
print("After Enqueue:")
linked_list.display()
linked_list.dequeue()
print("After Dequeue:")
linked_list.display()