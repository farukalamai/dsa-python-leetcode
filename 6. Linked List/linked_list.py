class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
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
    
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        # Have to understand properly
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        
    # def find_middle(self):
    #     temp = self.head
    #     if self.length == 0:
    #         return None
    #     elif self.length == 1:
    #         return temp
    #     elif (self.length % 2) == 0:
    #         n = (self.length//2)
    #         for _ in range(n):
    #             temp = temp.next
    #     else:
    #         n = (self.length + 1)//2
    #         for _ in range(n-1):
    #             temp = temp.next
    #     return temp
    
    # Not clear as much
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)

def remove_duplicates(self):
    if self.head is None:
        return
    node_values = set()  # set to store unique node values
    current_node = self.head
    node_values.add(current_node.value)
    while current_node.next:
        if current_node.next.value in node_values:  # duplicate found
            current_node.next = current_node.next.next
            self.length -= 1
        else:
            node_values.add(current_node.next.value)
            current_node = current_node.next
    self.tail = current_node

        
        




linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(20)




print(linked_list)

