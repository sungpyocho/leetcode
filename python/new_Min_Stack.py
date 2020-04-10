# # 아래의 Node를 사용한 일반 stack은 getMin()을 const time에 수행해내지 못한다.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.head = None
        
#     def is_empty(self):
#         if self.head:
#             return False
#         return True

#     def push(self, data: int) -> None:
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node        

#     def pop(self) -> None:
#         if self.is_empty():
#             return -1
#         self.head = self.head.next

#     def top(self) -> int:
#         if self.is_empty():
#             return -1
#         return self.head.data

#     def getMin(self) -> int:
#         minimum = self.top()
#         temp_ptr = self.head
        
#         while(temp_ptr.next):
#             temp_ptr = temp_ptr.next
#             if temp_ptr.data < minimum:
#                 minimum = temp_ptr.data
            
#         return minimum
    
class MinStack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()