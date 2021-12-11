nums = [2,3,1,1,4]

if 0 not in nums[:-1]:
    print("True_1")
    exit()
        
length = len(nums)

# find max index
max_index = 0
for i in range(length-1):
    if nums[i] == 0 and max_index <= i:
        print("False")
        exit()
    if max_index < i + nums[i]:
        max_index = i + nums[i]

print("True_3")