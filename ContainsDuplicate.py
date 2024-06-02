def containsDuplicate(nums):
    dict = {}
    for i,x in enumerate(nums):
        if x in dict:
            return True
        dict[x] = i
    return False

print(containsDuplicate([1,2,3,6]))