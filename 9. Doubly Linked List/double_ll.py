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
    
doubly_ll  = DoubleLinkedList()
doubly_ll.createDD(5)
doubly_ll.insertNode(0, 0)

doubly_ll.insertNode(2, 1)
doubly_ll.insertNode(6, 2)
print([node.value for node in doubly_ll])