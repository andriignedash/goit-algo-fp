class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def sorted_insert(sorted_list, new_node):
    if sorted_list.head is None or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = None
        sorted_insert(sorted_list, current)
        current = next_node
    linked_list.head = sorted_list.head

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list

# Приклад використання
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(2)
ll.print_list()  

reverse_linked_list(ll)
ll.print_list()  

insertion_sort(ll)
ll.print_list()  

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_ll = merge_sorted_lists(ll1, ll2)
merged_ll.print_list()  
