def sortColors(nums):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]]+=1
        else:
            dict[nums[i]] = 1
    sorted_nums = []
    for key in sorted(dict.keys()):
        sorted_nums.extend([key]*dict[key])
    return sorted_nums

print(sortColors([2,0,2,1,1,0]))
