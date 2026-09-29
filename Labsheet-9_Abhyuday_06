def solve(N, A):
    ans = 0
    for x in A:
        if x > 0:
            return -1
        else:
            ans = ans - x
    return ans
T = int(input("Enter number of test cases: "))

for i in range(T):
    N = int(input("Enter size of array: "))
    A = list(map(int, input("Enter array elements: ").split()))
    print("Answer:", solve(N, A))
