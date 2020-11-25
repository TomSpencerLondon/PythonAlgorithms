# calculates factorial of a positive integer
print("factorial")


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3))
print("------")
print("printFunc")


# Recursion and Memory
def printFunc(n):
    if n == 0:
        return 0
    else:
        print(n)
        return printFunc(n - 1)
    print(printFunc(n))


printFunc(4)

print("------")


def towersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towersOfHanoi(numberOfDisks - 1, startPeg, 6 - startPeg - endPeg)
        print("Move disk %d from peg %d to peg %d" % (numberOfDisks, startPeg, endPeg))
        towersOfHanoi(numberOfDisks - 1, 6 - startPeg - endPeg, endPeg)


towersOfHanoi(numberOfDisks=4)

print("------")
print("Problem 2: given an array check whether the array is in sorted order with recursion")


def isArrayInSortedOrder(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])


A = [127, 220, 246, 321, 454, 534, 565, 933]

print(isArrayInSortedOrder(A))
