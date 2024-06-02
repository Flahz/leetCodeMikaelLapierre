def removeDuplicates(nums):
    dict = {}
    k = 0
    for i,x in enumerate(nums):
        if x not in dict:
            nums[k] = x
            k = k + 1
            dict[x] = i #i meilleur runtime et True meilleur memory
    return k

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))