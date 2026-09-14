'''def threeSum(nums): 
    nums.sort() 
    print("Sorted array:", nums)

    result = [] 
    for i in range(len(nums) - 2): 
        if i > 0 and nums[i] == nums[i - 1]: 
            continue 
        left = i + 1 
        right = len(nums) - 1 
 
        while left < right: 
            total = nums[i] + nums[left] + nums[right] 
            if total == 0: 
                print("Triplet found:", nums[i], nums[left], nums[right])
                result.append([nums[i], nums[left], nums[right]]) 
                while left < right and nums[left] == nums[left + 1]: 
                    left += 1 
                while left < right and nums[right] == nums[right - 1]: 
                    right -= 1 
                left += 1 
                right -= 1 
            elif total < 0: 
                left += 1 
            else: 
                right -= 1 

    print("Final Result:", result)
    return result 

nums = [5, 6, -3, 8, 1, 2] 
threeSum(nums)'''

'''n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c'''

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)
n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
