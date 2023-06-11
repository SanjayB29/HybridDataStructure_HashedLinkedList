import random
import time
import matplotlib.pyplot as plt

def hash(val,arrlen,x):
    if(type(val)==str):
        sum=0
        for _ in [ord(char) for char in val]:
            sum+=_
    else:
        sum=val
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
    
    def insert(self, item):
        index=hash(item,self.size,self.x)
        if self.arr[index] is None:
            self.arr[index] = Node(item)
        else:
            currentNode=self.arr[index]
            while(currentNode.next is not None):
                currentNode=currentNode.next
            currentNode.next = Node(item)

    def delete(self, item):
        index = hash(item, self.size, self.x)
        current_node = self.arr[index]
        prev_node = None

        while current_node is not None:
            if current_node.key == item:
                if prev_node is None:
                    self.arr[index] = current_node.next
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


# Function to measure the time and space complexity for varying input size
def measure_complexity(max_size):
    sizes = []
    insert_time_complexities = []
    insert_space_complexities = []
    delete_time_complexities = []
    delete_space_complexities = []
    traverse_time_complexities = []
    traverse_space_complexities = []

    for size in range(1, max_size + 1):
        # Create a new HashedLinkedList instance
        hashlink = HashedLinkedList(size)

        # Measure the time complexity and space complexity for insert method
        start_time = time.process_time()
        for i in range(size):
            hashlink.insert(i)
        end_time = time.process_time()
        insert_time_complexity = end_time - start_time
        insert_space_complexity = size * 4  # Assuming each node consumes 4 bytes

        # Measure the time complexity and space complexity for delete method
        start_time = time.process_time()
        for i in range(size):
            hashlink.delete(i)
        end_time = time.process_time()
        delete_time_complexity = end_time - start_time
        delete_space_complexity = size * 4  # Assuming each node consumes 4 bytes

        # Measure the time complexity and space complexity for traverse method
        start_time = time.process_time()
        hashlink.traverse()
        end_time = time.process_time()
        traverse_time_complexity = end_time - start_time
        traverse_space_complexity = size * 4  # Assuming each node consumes 4 bytes

        sizes.append(size)
        insert_time_complexities.append(insert_time_complexity)
        insert_space_complexities.append(insert_space_complexity)
        delete_time_complexities.append(delete_time_complexity)
        delete_space_complexities.append(delete_space_complexity)
        traverse_time_complexities.append(traverse_time_complexity)
        traverse_space_complexities.append(traverse_space_complexity)

    # Plot the graph for insert method
    plt.plot(sizes, insert_time_complexities, label='Insert Time Complexity')
    plt.plot(sizes, insert_space_complexities, label='Insert Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Complexity')
    plt.title('Insert Method Complexity Analysis')
    plt.legend()
    plt.show()

    # Plot the graph for delete method
    plt.plot(sizes, delete_time_complexities, label='Delete Time Complexity')
    plt.plot(sizes, delete_space_complexities, label='Delete Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Complexity')
    plt.title('Delete Method Complexity Analysis')
    plt.legend()
    plt.show()

    # Plot the graph for traverse method
    plt.plot(sizes, traverse_time_complexities, label='Traverse Time Complexity')
    plt.plot(sizes, traverse_space_complexities, label='Traverse Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Complexity')
    plt.title('Traverse Method Complexity Analysis')
    plt.legend()
    plt.show()

# Example usage
max_input_size = 100
measure_complexity(max_input_size)
