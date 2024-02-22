"""
What is Linked List in Python
A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with each other. 
A node contains two things first is data and second is a link that connects it with another node.
Below is an example of a linked list with four nodes and each node contains character data and a link to another node.
Our first node is where head points and we can access all the elements of the linked list using the head.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()

# Insert at the beginning
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(1)

# Display the linked list
linked_list.display()  # Output: 1 -> 2 -> 3 -> None

# Insert at the end
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)

# Display the linked list after insertion at the end
linked_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
