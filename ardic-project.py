operations = input("please enter operations:")
# operations = "3+5*3/7-5+6"
print(eval(operations), "result of eval function for correction")
stack = [i for i in operations]
index, result = 0, 0
size = len(stack)
def stack_pop(stack, index):
    """
    Takes stack as a list and index,
    It pops item from stack and subtracts -1 from index.
    Return: stack as a list and index 
    """
    stack.pop(index+1)
    stack.pop(index-1)
    stack[index-1] = result
    index = -1
    return stack, index

while size != 1:
    if '*' in stack or '/' in stack:

        if stack[index] == '/':
            result = float(stack[index-1])/float(stack[index+1])
            stack, index = stack_pop(stack, index)
            continue

        elif stack[index] == '*':
            result = float(stack[index-1])*float(stack[index+1])
            stack, index = stack_pop(stack, index)
            continue

    elif "-" in stack or "+" in stack:
        if stack[index] == '+':
            result = float(stack[index-1])+float(stack[index+1])
            stack, index = stack_pop(stack, index)
            continue

        elif stack[index] == '-':
            result = float(stack[index-1])-float(stack[index+1])
            stack, index = stack_pop(stack, index)
            continue

    size = len(stack)
    index += 1
print(result, "result of algorithm")
print(*stack)
