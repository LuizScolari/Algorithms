def maximunLengthSubstring(array):
    l, r = 0, 0
    dic = {}
    max = 1
    dic[array[r]] = 1

    while r < len(array)-1:
        r += 1
        if dic.get(array[r]):
            dic[array[r]] += 1
        else:
            dic[array[r]] = 1
        while dic[array[r]] == 3:
            dic[array[l]] -= 1
            l += 1
        if len(array[l:r+1]) > max:
            max = len(array[l:r+1])
    print(max)

maximunLengthSubstring("bcbbbcba")