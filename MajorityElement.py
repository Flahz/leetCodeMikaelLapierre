def majorityElement(nums):
    nums_freq = {}

    for char in nums:
        nums_freq[char] = nums_freq.get(char,0) + 1
    size_nums = len(nums)
    for key,value in nums_freq.items():
        if value > size_nums/2:
            return key
print(majorityElement([3,2,3]))