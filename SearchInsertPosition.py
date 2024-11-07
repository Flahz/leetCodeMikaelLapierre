def searchInsert(nums, target):
    valueMin = 9999
    indexMin = 0
    for i in range(len(nums)):
        if valueMin > abs(target - nums[i]): 
            valueMin = target - nums[i]
            if target < nums[i]:
                indexMin = i
            else:
                indexMin = i + 1
        if target - nums[i] == 0:
            return i
    return indexMin

print(searchInsert([1,3,5,6],0))

