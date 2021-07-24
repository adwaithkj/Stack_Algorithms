# Given an array of value print a corresponding array with values
# that shows the corresponding values' nearest greater value to the
# right
# if nothing exists to the right of a value, let it's corresponding
# value be -1

def NGLbruteforce(arr):
    newarr = []
    for i, j in enumerate(arr):

        for k in range(i, -1, -1):
            if arr[k] > j:
                newarr.append(arr[k])
                break
            if k == 0:
                newarr.append(-1)

    return newarr


def NGL(arr):

    stack = []
    top = 0
    newarr = []

    for i in range(len(arr)):
        if i == 0:
            newarr.append(-1)
            stack.append(arr[i])
            top = 0
        else:
            if stack[top] < arr[i]:
                while stack != [] and stack[top] < arr[i]:
                    stack.pop()
                    top -= 1
                if stack == []:
                    newarr.append(-1)
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


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    # print("Time taken for Brute force is ")
    # print(timeit.timeit("NGRbruteforce(arr)"))

    # print("Time taken for Stack is ")
    # print(timeit.timeit("NGR(arr)"))
    print(NGLbruteforce(arr))
    print(NGL(arr))
