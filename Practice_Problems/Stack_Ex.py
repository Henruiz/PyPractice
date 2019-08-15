"""" Making a stack using single linked list """

class LL_to_Stack(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, front):
        front = LL_to_Stack(front)
        front.next = self
        return front

    # def peak(self):
    #     if self == None:
    #         return None
    #     else:
    #         return self.data

    def pop(self):
        data = self.data
        nxt = self.next
        if nxt is None:
            self.data = self.next = None
        else:
            self.data = nxt.data
            self.next = nxt.next
            nxt.next = None
        return data

    def print(self):
        x = self
        if x == None:
            print("Empty")
        else:
            print(x.data)
        while x.next != None:
            x = x.next
            print(x.data)


x = LL_to_Stack(1)
x = x.insert(2)
x = x.insert(3)
print("Will print out 3, 2, 1: ")
x.print()
print("Will print out 2, 1: ")
x.pop()
x.print()

