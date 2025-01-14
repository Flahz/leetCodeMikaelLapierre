def pivotIndex(nums):
    sum = 0
    sum2 = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    for i in range(len(nums)):
        pivot = nums[i]
        if sum - pivot - sum2 == sum2:
            return i
        sum2 = sum2 + pivot

    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))  # Résultat attendu : 3
print(pivotIndex([1, 2, 3]))           # Résultat attendu : -1
print(pivotIndex([2, 1, -1]))          # Résultat attendu : 0
print(pivotIndex([-1, -1, -1, -1, -1, 1]))  # Résultat attendu : -1
print(pivotIndex([-1, -1, -1, -1, 0, 1]))   # Résultat attendu : 1
print(pivotIndex([-1, -1, -1, 0, -1, 0]))   # Résultat attendu : -1
