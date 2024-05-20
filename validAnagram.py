def isAnagram(s,t):
    s_frequ = {}
    t_frequ = {}

    for char in s:
        s_frequ[char] = s_frequ.get(char,0) + 1
    for char in t:
       t_frequ[char] = t_frequ.get(char,0) + 1 
    return s_frequ == t_frequ

print(isAnagram("aaaa","aaaa"))
print(isAnagram("anagrgam","ngagaram"))
#print(isAnagram("rat","car"))