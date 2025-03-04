def sorting(array):
    siz = len(array)
    for _ in range(len(array)):
        for i in range(siz-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        siz -= 1
    return array

array = [5,4,3,2,1]
print(sorting(array))