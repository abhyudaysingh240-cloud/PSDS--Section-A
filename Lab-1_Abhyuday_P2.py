import numpy as np
a = []
for i in range(5):
    num = int(input("Enter a number: "))
    a.append(num)
arr = np.array(a)
print("Initial array:", arr)
while len(arr) > 0:
    popped = arr[0]         
    arr = np.delete(arr, 0) 
    print("Popped:", popped)
    print("Remaining array:", arr)