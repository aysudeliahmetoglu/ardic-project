
# from collections import deque

# stack=deque

# operations=input("please enter operations:")
# stack.__add__(self, other)(operations)
# size=stack.__sizeof__(self)()
# print(size)

# if stack.empty():
#     print("geçersiz işlem")
# # print(stack)
# # for i in range(1,size):
# #     print(i)

from collections import deque
myStack = deque()
stack=[]
operations=input("please enter operations:")
operators={'*','/','+','-'}
stack.append(operations)

myStack.append(operations[0])
myStack.append(operations[1])
myStack.append(operations[2])
myStack.append(operations[3])
myStack.append(operations[4])
myStack=int(myStack)

print(myStack)
# for i in range(0,10):
#     # print(myStack[i])
#     if myStack[1]=='*':
#         result=myStack[0]+myStack[2]
#         print(result)

#mutliply functions
# def Carp(myStack) : 
      
     
#     result = 1
#     for x in myStack: 
#          result = result * x  
#     return result  
# Carp(myStack)