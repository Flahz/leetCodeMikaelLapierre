
def plusOne(digits):
    size = len(digits)
    multiplier = 10**(size-1)
    sum = 0
    for digit in digits:
        sum += digit * multiplier
        multiplier //= 10  # Use integer division here to keep multiplier as an integer
    sum += 1
    sumInt = int(sum)
    digits_list = [int(lol) for lol in str(sumInt)]
    return digits_list

    
    


digits = [1,2,3,4,5]

print(plusOne(digits))

