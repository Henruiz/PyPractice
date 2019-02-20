class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node to the front
    def front(self, input):
        NewNode = Node(input)
        NewNode.next = self.head
        self.head = NewNode

    # Function to add a node in the midde
    def middle(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    # Function to remove node
    def RemoveNode(self, input):

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

    def LListprint(self):
        printval = self.head
        while printval:
            print(printval.data),
            printval = printval.next


llist = SingleLinkedList()
llist.front("Mon")
llist.front("Tue")
llist.front("Wed")
llist.front("Thu")
llist.front("Fri")
llist.RemoveNode("Tue")
llist.LListprint()
print('---------------------')
llist.middle(llist.head.next, "middle")
llist.LListprint()