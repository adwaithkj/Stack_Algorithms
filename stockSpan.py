# This is a variation of the 4 types of NGR and NGL
# Let us move on to the problem
# we are given an array say [100,,80,60,70,75,85]
# we have to output for a given day the consecutive smaller or equal to
# so the for the array [100,80,60,75,85] the result should be the
# following array      [1  ,1 ,2 ,2 ,4 ]

def stockSpan(arr):
    stack = []
    top = None
    newarr = []
    count = 0
    for i in range(len(arr)):

        if stack == []:
            stack.append(arr[i])
            top = 0
            newarr.append(1)
        elif stack[top] < arr[i]:
            while stack != [] and stack[top] < arr[i]:
                stack.pop()
                top -= 1
                count += 1
            stack.append(arr[i])
            top += 1
            newarr.append(count+1)
        else:
            stack.append(arr[i])
            top += 1
            newarr.append(1)

        print(stack)

    return newarr


if __name__ == '__main__':

    arr = [10, 4, 5, 90, 120, 80]
    print(stockSpan(arr))
