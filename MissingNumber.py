def missingNumber(nums):
    sommeTotal = 0
    sommeNums = 0
    for i in range(len(nums)+1):
        sommeTotal = sommeTotal + i
        if i in range(len(nums)):
            sommeNums = sommeNums + nums[i]
    
    return sommeTotal-sommeNums

print(missingNumber([3,0,1]))
