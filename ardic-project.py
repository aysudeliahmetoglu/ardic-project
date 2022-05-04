stack=[]
operations=input("please enter operations:")
operators=['*','/','+','-']
stack.append(operations)
for i in operations:
    stack.append(i)
print(stack)


if stack[2]=='+':
    result=int(stack[1])+int(stack[3])
    print( result)
elif stack[2]=='-':
    result=int(stack[1])-int(stack[3])
    print(result)
elif stack[2]=='*':
    result=int(stack[1])*int(stack[3])
    print(result)
elif stack[2]=='/':
    result=int(stack[1])/int(stack[3])
    print(result)    
