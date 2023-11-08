class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDD(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node 
        return "DD Done"
    
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node can't be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                temNode = self.head
                index = 0
                while index < location -1:
                    temNode = temNode.next
                    index += 1
                newNode.next = temNode.next
                newNode.prev = temNode
                newNode.next.prev = newNode
                temNode.next = newNode

    def traverseDL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next

    def reverseDL(self):
        if self.head is None:
            print("There is not any element for traverrse")
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev

    def searchDL(self, target):
        if self.head is None:
            print("This value is not exist")
        else:
            temp = self.head
            while temp:
                if temp.value == target:
                    return temp.value
                temp = temp.next

            return "This node doesn't exist"
        
    def delete(self, location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current = self.head
                index = 0
                while index < location -1:
                    current = current.next
                    index += 1
                current.next = current.next.next
                current.next.prev = current
            print("The node has been sucessfully deleted")






doubly_ll  = DoubleLinkedList()
doubly_ll.createDD(5)
doubly_ll.insertNode(0, 0)

doubly_ll.insertNode(2, 1)
doubly_ll.insertNode(6, 2)
print([node.value for node in doubly_ll])
doubly_ll.delete(1)
print([node.value for node in doubly_ll])
