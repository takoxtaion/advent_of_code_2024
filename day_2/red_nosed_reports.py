# part 1

# with open('day_2/input.txt', 'r') as file:
#     lines = file.read().strip().split("\n")

# differs = [1,2,3]

# counter = 0

# for line in lines:
#     nums = [int(i) for i in line.split()]

#     def isMonotonic(nums):
#         is_increasing = all(nums[i] > nums[i-1] for i in range(1, len(nums)))
#         is_decreasing = all(nums[i] < nums[i-1] for i in range(1, len(nums)))

#         return is_increasing or is_decreasing
    
#     def is_differ(nums):
#         dif = all(abs(nums[i]-nums[i-1]) in differs for i in range(1, len(nums)))

#         return dif
    
#     first_check = isMonotonic(nums)
#     second_check = is_differ(nums)

#     if first_check == True and second_check == True:
#         counter += 1

# print(counter)

#part 2

with open('day_2/input.txt', 'r') as file:
    lines = file.read().strip().split("\n")

differs = [1,2,3]

counter = 0

for line in lines:
    nums = [int(i) for i in line.split()]


    def isMonotonic(nums):
        is_increasing = all(nums[i] > nums[i-1] for i in range(1, len(nums)))
        is_decreasing = all(nums[i] < nums[i-1] for i in range(1, len(nums)))
        return is_increasing or is_decreasing         


    def is_differ(nums):
        dif = all(abs(nums[i]-nums[i-1]) in differs for i in range(1, len(nums)))
        return dif
    
    def new_check(nums):
        for i in range(len(nums)):
            temp = nums.pop(i)
            if isMonotonic(nums) and is_differ(nums):
                nums.insert(i, temp)
                return True
            nums.insert(i, temp)
        return False

    if new_check(nums):
        counter +=1

print(counter)

