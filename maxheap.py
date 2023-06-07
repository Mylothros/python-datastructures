class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    
    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max
    
    def __swap(self, i, j):
        self.heap[i], self.heap[i] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
    
    def __str__(self):
        return str(self.heap)
    
m = MaxHeap([95, 3, 21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())  
print(m)

# use heapify:

# # Python3 program to demonstrate working of heapq
  
# from heapq import heappop, heappush, heapify
  
# # Creating empty heap
# heap = []
# heapify(heap)
  
# # Adding items to the heap using heappush
# # function by multiplying them with -1
# heappush(heap, -1 * 10)
# heappush(heap, -1 * 30)
# heappush(heap, -1 * 20)
# heappush(heap, -1 * 400)
  
# # printing the value of maximum element
# print("Head value of heap : " + str(-1 * heap[0]))
  
# # printing the elements of the heap
# print("The heap elements : ")
# for i in heap:
#     print((-1*i), end=" ")
# print("\n")
  
# element = heappop(heap)
  
# # printing the elements of the heap
# print("The heap elements : ")
# for i in heap:
#     print(-1 * i, end = ' ')
