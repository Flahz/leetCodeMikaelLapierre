def sortColors(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    T1 = sortColors(nums[:mid])
    T2 = sortColors(nums[mid:])
    return Fusionner(T1,T2)


def Fusionner(T1,T2):
    arrayFusion = []
    i = 0
    j = 0
    while i < len(T1) and j < len(T2):
        if T1[i] >= T2[j]:
            arrayFusion.append(T2[j])
            j += 1
        else:
            arrayFusion.append(T1[i])
            i += 1
    while i < len(T1) or j < len(T2):
        if i < len(T1):
            arrayFusion.append(T1[i])
            i +=1
        else:
            arrayFusion.append(T2[j])
            j+=1
    return arrayFusion

print(sortColors([2,0,2,1,1,0]))
