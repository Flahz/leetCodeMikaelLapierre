def twoSum(nums,target):
    dict = {}
    for i, x in enumerate(nums):
        element = target - x
        if element in dict:
            return [dict[element],i]
        dict[x] = i
    return 0   
print(twoSum([2,7,11,15],9))
            
