import numpy as np
a=[]
for i in range(5):
    i=int(input("Enter a number: ")) 
    a.append(i)
arr = np.array(a)
while len(arr) > 0:
    popped = arr[-1]      
    arr = np.delete(arr, -1) 
    print("Popped:", popped)
    print("Remaining array:", arr)