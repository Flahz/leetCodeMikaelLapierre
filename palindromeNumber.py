def isPalindrome(x):
    x_string = str(x)
    for i in range(len(x_string)):
        if x_string[i] != x_string[len(x_string)-1-i]:
            return False
    return True

print(isPalindrome(1234554321))
