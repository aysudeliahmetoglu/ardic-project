# operations = input("please enter operations:")
operations = "-12.3-7.2*3"

print(eval(operations), "result of eval function for correction")
print(operations)
# stack = [i for i in operations]
# index, result = 0, 0
# size = len(stack)
# def stack_pop(stack, index):
#     """
#     Takes stack as a list and index,
#     It pops item from stack and subtracts -1 from index.
#     Return: stack as a list and index
#     """
#     stack.pop(index+1)
#     stack.pop(index-1)
#     stack[index-1] = result
#     index = -1
#     return stack, index

# while size != 1:
#     if '*' in stack or '/' in stack:

#         if stack[index] == '/':
#             result = float(stack[index-1])/float(stack[index+1])
#             stack, index = stack_pop(stack, index)
#             continue

#         elif stack[index] == '*':
#             result = float(stack[index-1])*float(stack[index+1])
#             stack, index = stack_pop(stack, index)
#             continue

#     elif "-" in stack or "+" in stack:
#         if stack[index] == '+':
#             result = float(stack[index-1])+float(stack[index+1])
#             stack, index = stack_pop(stack, index)
#             continue

#         elif stack[index] == '-':
#             result = float(stack[index-1])-float(stack[index+1])
#             stack, index = stack_pop(stack, index)
#             continue

#     size = len(stack)
#     index += 1
# print(result, "result of algorithm")
# print(*stack)


def get_number(stack):
    operators = ["*", "/", "+", "-"]
    x = (operations.replace("*", ",").replace("/",
         ",").replace("+", ",").replace("-", ",").split(","))
    return [i for i in x if i != ""]


seen = []


def get_sign(stack, number):
    seen.append(number)
    if len([i for i, n in enumerate(seen) if n == number]) > 1:
        stack = stack.replace(number, "", 1)
    index = stack.index(number)
    if index != 0:
        print((stack[index-1], "+", number, index, stack), "(stack[index-1], "+", number)")
        return (stack[index-2] if not stack[index-2].isdigit() else "", stack[index-1], number) if stack[index-1] in ["+", "-"] else (stack[index-1], "+", number)
    return "+"


numbers = get_number(operations)


xxx = [get_sign(operations, item) for index, item in enumerate(numbers)]


def get_operation(stack):
    return stack[1] if stack[0] == "" else stack[0]


index_counter = 1
while True:
    print(xxx)
    if isinstance(xxx, int) or isinstance(xxx, float):
        break
    print(("*" in [j for i in xxx for j in i] or "/" in [j for i in xxx for j in i]), [j for i in xxx for j in i])
    if len(xxx) > index_counter and ("*" in [j for i in xxx for j in i] or "/" in [j for i in xxx for j in i]):
        # print(get_operation(xxx[index_counter]), "get_operation(xxx[index_counter])")
        if get_operation(xxx[index_counter]) in ["*", "/"]:
            print(xxx)
            if xxx[index_counter][0] == "*":
                a = float(f"{xxx[index_counter-1][1]}{xxx[index_counter-1][2]}") * \
                    float(f"{xxx[index_counter][1]}{xxx[index_counter][2]}")
            else:
                a = float(f"{xxx[index_counter-1][1]}{xxx[index_counter-1][2]}") / \
                    float(f"{xxx[index_counter][1]}{xxx[index_counter][2]}")
            xxx[index_counter] = ("", str(a)[0] if not str(a)[0].isdigit(
            ) else "+", str(a) if str(a)[0].isdigit() else str(a)[1:])
            xxx.remove(xxx[index_counter-1])

            index_counter = 1
            print(xxx)
            continue

    else:
        if len(xxx) == 1:
            break
        a = float(f"{xxx[index_counter-1][1]}1")*float(xxx[index_counter-1][2]) + \
            float(f"{xxx[index_counter][1]}1")*float(xxx[index_counter][2])
        xxx[index_counter] = ("", str(a)[0] if not str(a)[0].isdigit(
        ) else "+", str(a) if str(a)[0].isdigit() else str(a)[1:])
        xxx.remove(xxx[index_counter-1])
        index_counter = 1
        continue

    index_counter += 1

print(f"{xxx[0][1]}{xxx[0][2]}")
