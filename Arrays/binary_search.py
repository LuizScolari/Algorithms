def binary_search(array, n):
    t, r = len(array)-1, 0
    steps = 0
    while r <= t:
        mid = (t+r) // 2
        steps += 1

        if array[mid] == n:
            print(steps)
            return
        elif array[mid] < n:
            r = mid + 1
        else: 
            t = mid
    print("-1")


binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 5)
binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40], 5)