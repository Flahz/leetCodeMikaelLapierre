def generate(numsRows):
    
    top_value = numsRows[-1]
    if isinstance(numsRows, int):
        return generate([[1]])
    i=1
    numsAdd = []
    for i in range(len(top_value)):
        if i == 1:
            numsAdd[i] = 1
        if i == len(top_value):
            numsAdd[i] = 1
        else:
            numsAdd[i]= top_value[i] + top_value[i-1]
    return generate(numsAdd)

print(generate(5))