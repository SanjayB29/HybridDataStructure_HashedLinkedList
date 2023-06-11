import random


def hash(val,arrlen,x):
    if(type(val)==str):
        sum=0
        for _ in [ord(char) for char in val]:
            sum+=_
    else:
        sum=val
        #Multiplication Method
    a=(sum*x)%1
    a=(a*arrlen)//1
    return int(a)


class Node:
    def __init__(self, key):
        self.key = key
        
        self.next = None
        
class HashedLinkedList:
    def __init__(self,size):
        self.arr = []
        self.size = size
        for i in range(size):
            self.arr.append(None)
        self.x=1/random.random()
        # self.x=1/63
    
    def insert(self, item):
        index=hash(item,self.size,self.x)
        if self.arr[index] is None:
            self.arr[index] = Node(item)
        else:
            currentNode=self.arr[index]
            while(currentNode.next is not None):
                currentNode=currentNode.next
            currentNode.next = Node(item)
        return

    def delete(self, item):
        index = hash(item, self.size, self.x)
        current_node = self.arr[index]
        prev_node = None

        # Iterate through the linked list at the given index
        while current_node is not None:
            if current_node.key == item:
                # Case 1: Item is found at the head of the linked list
                if prev_node is None:
                    self.arr[index] = current_node.next
                # Case 2: Item is found in the middle or at the end of the linked list
                else:
                    prev_node.next = current_node.next
                return

            prev_node = current_node
            current_node = current_node.next
    
    def traverse(self):
        items = []
        for i in range(self.size):
            current_node = self.arr[i]
            while current_node:
                items.append(current_node.key)
                current_node = current_node.next
        return items

    def print_list(self):
        for _ in range(50):
            print("-",end="")
        print()
        for i in range(self.size):
            print(f"Index {i}:",end=" -> ")
            current_node = self.arr[i]
            while current_node:
                print(f"{current_node.key}",end="  ->  ")
                current_node = current_node.next
            if(current_node is None):
                print("None")
        for _ in range(50):
            print("-",end="")
        print()
            

# Example usage:
hashlink = HashedLinkedList(10)
hashlink.insert(1)
hashlink.insert(5)
hashlink.insert(10)
hashlink.insert(20)
hashlink.insert(15)
hashlink.insert(7)
hashlink.insert(3)
hashlink.insert(9)
hashlink.insert(18)
hashlink.insert(25)
hashlink.insert(13)
hashlink.insert(4)
hashlink.insert(8)
hashlink.insert(12)
hashlink.insert(6)
hashlink.insert(22)
hashlink.insert(17)
hashlink.insert(11)
hashlink.insert(16)
hashlink.insert(2)



hashlink.print_list()

all_items = hashlink.traverse()
print(all_items)
    
