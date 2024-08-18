class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        i = 0
        while fast is not None:
            fast = fast.next
            if i % 2 == 0:
                slow = slow.next
            if fast is not None:
                fast = fast.next
            i += 1
        if i == 0:
            return
        if i == 1:
            return self.head
        if i % 2 == 0:
            return slow.next
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)


print(my_linked_list.find_middle_node().value)

"""
    EXPECTED OUTPUT:
    ----------------
    3

"""