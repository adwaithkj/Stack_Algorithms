def NSR(arr):
    stack = []
    newarr = []
    top = None
    arr.reverse()

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
    newarr.reverse()
    return newarr


def NSRbruteforce(arr):
    pass


if __name__ == '__main__':
    arr = [4, 5, 2, 10, 8]
    print(arr)

    print(NSRbruteforce(arr))
    print(NSR(arr))
