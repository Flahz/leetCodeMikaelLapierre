def strStr(haystack, needle):
    capture = False
    #print(len(needle))
    for i in range(len(haystack)):
        k = i
        for j in range(len(needle)):
            if k != len(haystack):
                if haystack[i] == needle[j]:
                    capture = True
                if capture and haystack[k] != needle[j]:
                    capture = False
                if capture and haystack[k] == needle[j]:
                    k +=1
                if k-i == len(needle) and capture:
                    return i
            
            
    return -1

print(strStr("leetcode","leeto"))
        