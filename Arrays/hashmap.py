def firstUniqChar(array):
    dic = {}
    for i in range(len(array)):
        if dic.get(array[i]):
            dic[array[i]][1] += 1
        else: 
            dic[array[i]] = [i, 1]
    
    for j in range(len(array)):
        if dic[array[j]][1] == 1:
            return dic[array[j]][0]
    return -1

print(firstUniqChar("aabbccd"))