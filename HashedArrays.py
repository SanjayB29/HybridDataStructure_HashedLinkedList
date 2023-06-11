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


class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.x = 1 / random.random()

    

    def insert(self, key):
        index = hash(key,self.size,self.x)
        self.buckets[index].append(key)

    def delete(self, key):
        index = hash(key,self.size,self.x)
        bucket = self.buckets[index]
        for i, k in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
    
    def traverse(self):
        items = []
        for bucket in self.buckets:
            for key in bucket:
                items.append(key)
        return items    

    def print_map(self):
        for _ in range(50):
            print("-",end="")
        print()
        for i in range(self.size):
            print(f"Index {i}:",end=" -> ")
            for k in self.buckets[i]:
                print(f"{k}",end="  ->  ")
            print("None")
        for _ in range(50):
            print("-",end="")
        print()


# Example usage:
hashlink = HashMap(10)

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


hashlink.print_map()

hashlink.delete(16)

print(hashlink.traverse())

hashlink.print_map()
