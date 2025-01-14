def pivotIndex(nums):
    dictFirstHalf = {}
    dictSecondHalf = {}
    sumCroissant = 0
    sumDecroissant = 0
    i = 0
    while i<len(nums):
        sumCroissant = sumCroissant + nums[i]
        sumDecroissant = sumDecroissant + nums[len(nums) - i]
        dictFirstHalf[i] = sumCroissant
        dictSecondHalf[]
        i+=1
    while i < len(nums):
        sumSecondHald = sumSecondHald + nums[i]
        i+=1
    if sumSecondHald == sumFirtHalf:
        return i
    return -1



print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))