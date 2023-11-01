class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = next

class CSLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        elif index == 0:
            new_node.next = temp_node
            self.head = new_node
            self.tail.next = new_node
        elif self.length == index:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node       
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        temp = self.head
        while temp is not None:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
            return False
        
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        temp = self.head
        if temp is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail = self.head
            temp.next = None
        self.length -= 1
        return temp
    
    def pop(self):
        popped_node = self.tail
        temp = self.head
        if temp is None:
            return None
        elif self.length ==1:
            self.head = self.tail = None
        else:
            while temp is not popped_node:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index <0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node
    
    def delete(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

        

    







cs_ll = CSLinkedList()
cs_ll.append(10)
cs_ll.append(20)
cs_ll.append(30)
cs_ll.prepend(40)
cs_ll.insert(4, 50)



print(cs_ll)
cs_ll.delete()
print(cs_ll)