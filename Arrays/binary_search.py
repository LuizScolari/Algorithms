## FIRST IMPLEMENTATION
def binary_search(array, n):
    t = len(array)//2 - 1
    r = 0
    steps = 0
    while n != array[t]:
        if n < array[t]:
            dif = (t - r)//2 + 1
            t = int(t - dif)
        else:
            dif = (t - r)//2 + 1
            r = t
            t = t + dif
        steps += 1
    print(steps+1)

binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 17)