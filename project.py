arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr3 = []
for x in range(0, 10):
    x = arr1[x]+arr2[x]
    arr3.append(x)
print(arr3)
arrlen = len(arr3)
print(arrlen)
