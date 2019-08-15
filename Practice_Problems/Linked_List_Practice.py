
# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Linked List class contains a Node object
class LinkedList:

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node after current node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print
            "The given previous node must inLinkedList."
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Function to insert a new node at the end
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # Function to add a node in the middle
    def insertMiddle(self, middle_node, newdata):
            if middle_node is None:
                print("The mentioned node is absent")
                return

            NewNode = Node(newdata)
            NewNode.next = middle_node.next
            middle_node.next = NewNode

        # Function to remove node
    def removeNode(self, input):

        head_value = self.head

        if head_value is not None:
            if head_value.data == input:
                self.head = head_value.next
                HeadVal = None
                return

        while head_value is not None:
            if head_value.data == input:
                break
            prev = head_value
            head_value = head_value.next

        if head_value == None:
            return
        prev.next = head_value.next
        HeadVal = None

    # Function to reverse the Linked List
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# Start with the empty list
llist = LinkedList()

# Insert 6.  So linked list becomes 6->None
llist.insertFront(6)

# Insert 7 at the beginning. So linked list becomes 7->6->None
llist.insertFront(7)

# Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.insertFront(1)

# Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.insertEnd(4)

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)

# Insert 9, after 7. So linked list becomes 1-> 7-> middle-> 8-> 4->
llist.insertMiddle(llist.head.next, 'middle')

print('Created linked list is:',)
llist.printList()
print('Reversing the Linked List: ')
llist.reverse()
llist.printList()
