stack=[]
operations=input("please enter operations:")
operators=['*','/','+','-']

# stack.append(operations)

for i in operations:
    stack.append(i)
print(stack)
toplam=0
index=0
size=len(stack)

while (size>1):
    if stack[index] =='/':
        toplam = int(stack[index-1])/int(stack[index+1])
        
        stack.pop(index+1)
        stack.pop(index-1)
        stack[index-1]=toplam 
        i+=1
        index=0
        

    if stack[index] =='*':
        toplam = int(stack[index-1])*int(stack[index+1])
        
        stack.pop(index+1)
        stack.pop(index-1)
        stack[index-1]=toplam 

                  
       
    size=len(stack) 
    
    index+=1
print(toplam)
print(stack)




# if stack[2]=='+':
#     result=int(stack[1])+int(stack[3])
#     print( result)
# elif stack[2]=='-':
#     result=int(stack[1])-int(stack[3])
#     print(result)
# elif stack[2]=='*':
#     result=int(stack[1])*int(stack[3])
#     print(result)
# elif stack[2]=='/':
#     result=int(stack[1])/int(stack[3])
    # print(result)    
