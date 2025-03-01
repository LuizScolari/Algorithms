def binary_search(array, n, r, t):
    while r <= t:
        mid = (t+r) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            r = mid + 1
        else: 
            t = mid
    return -1

def exponential_search(array, n):
    if array[0] == n:
        return 0
    siz = len(array)
    r = 1
    
    while r < siz and array[r] < n:
        r = r*2
    
    if r > siz:
        r = siz - 1 
    
    if array[r] == n:
        return r
    
    return(binary_search(array, n, r//2, r))

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
n = 29
print(exponential_search(array, n))