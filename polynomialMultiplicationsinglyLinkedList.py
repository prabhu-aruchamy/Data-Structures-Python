class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        presNode = self.head
        while presNode:
            print(presNode.data)
            presNode = presNode.next

    def addNode(self, data):
        newNode = Node(int(data))
        if self.head is None:
            self.head = newNode
            return True

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def sizeofll(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def deleteNode(self, key):

        presNode = self.head

        if presNode and presNode.data == key:
            self.head = presNode.next
            presNode = None
            return

        prev = None
        while presNode and presNode.data != key:
            prev = presNode
            presNode = presNode.next

        if presNode is None:
            print("Value not found in the list!")
            return

        prev.next = presNode.next
        presNode = None

    def reverseoflist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev

    def calculateval(self, x, y):
        print(pow(x, y), "\n")
        z = pow(x, y)

    def calcpoly(self):
        h = self.head
        n = h.next
        cube = pow(h, n)
        h = n.next
        n = h.next
        square = pow(h, n)
        h = n.next
        n = h.next
        powone = pow(h, n)
        const = n.next
        print(int(cube + square + powone + const))



myList = LinkedList()
q3 = int(input("Enter the coefficient of cube: "))
myList.addNode(q3)
myList.addNode(3)
myList.calculateval(q3, 3)
myList.printList()

q2 = int(input("Enter the coefficient of square: "))
myList.addNode(q2)
myList.addNode(2)
myList.calculateval(q2, 2)
myList.printList()

q1 = int(input("Enter the coefficient of x: "))
myList.addNode(q1)
myList.addNode(1)
myList.calculateval(q1, 1)
myList.printList()

q = int(input("Enter the constant: "))
myList.addNode(q)
myList.printList()
myList.calcpoly()
