array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

t=0

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        t+=1
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(t)