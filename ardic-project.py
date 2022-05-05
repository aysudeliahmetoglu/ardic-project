stack=[]
operations=input("please enter operations:")
# operators=['*','/','+','-']

# stack.append(operations)

for i in operations:
    stack.append(i) 
print(stack)
toplam=0
index=0
size=len(stack)

while (size!=1):
    if '*' or '/' in stack:

        if stack[index] =='/':
            print("bölme")
            toplam = int(stack[index-1])/int(stack[index+1])
            
            stack.pop(index+1)
            stack.pop(index-1)
            stack[index-1]=toplam 
            index=-1
            print(stack)

        elif stack[index] =='*':
            toplam = int(stack[index-1])*int(stack[index+1])
            
            stack.pop(index+1)
            stack.pop(index-1)
            stack[index-1]=toplam 
            index=-1
    elif "-" or "+" in stack:
        if stack[index] =='+':
            toplam = int(stack[index-1])+int(stack[index+1])
            
            stack.pop(index+1)
            stack.pop(index-1)
            stack[index-1]=toplam 
            index=-1


        elif stack[index] =='-':
            toplam = int(stack[index-1])-int(stack[index+1])
            
            stack.pop(index+1)
            stack.pop(index-1)
            stack[index-1]=toplam 
            index=-1
                
        
    size=len(stack) 
    
    index+=1
print(toplam)
print(stack)
   
