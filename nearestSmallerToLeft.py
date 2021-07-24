def NSL(arr):
    stack = []
    newarr = []
    top = None

    for i in range(len(arr)):
        if i == 0:
            newarr.append(-1)
            stack.append(arr[i])
            top = 0
        else:
            if stack[top] > arr[i]:
                while stack != [] and stack[top] > arr[i]:
                    stack.pop()
                    if top != 0:
                        top -= 1
                if stack == []:
                    newarr.append(-1)
                    stack.append(arr[i])
                    top = 0
                else:
                    newarr.append(stack[top])
                    stack.append(arr[i])
                    top += 1
            else:

                newarr.append(stack[top])
                top += 1
                stack.append(arr[i])

    return newarr


def NSLbruteforce(arr):
    pass


if __name__ == '__main__':
    arr = [4, 5, 2, 10, 8]
    # print("Time taken for Brute force is ")
    # print(timeit.timeit("NGRbruteforce(arr)"))

    # print("Time taken for Stack is ")
    # print(timeit.timeit("NGR(arr)"))
    print(NSLbruteforce(arr))
    print(NSL(arr))
