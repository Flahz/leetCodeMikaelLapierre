def generate(numRows):
    list1 = [[1]]
    n = 2
    while n < numRows + 1:
        list2 = []
        for k in range(n):
            if k == 0:
                list2.append(1)
            elif k == n-1:
                list2.append(1)
            else:
                list2.append(list1[n-2][k-1] + list1[n-2][k])
        list1.append(list2)
        n += 1
    return list1

print(generate(5))
    

   

