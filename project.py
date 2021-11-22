arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr3 = []
for x in range(0, 10):
    x = arr1[x]+arr2[x]
    arr3.append(x)
print(arr3)
arrlen = len(arr3)
print(arrlen)
print("___________________________")

arr4 = [10, 11, 12, 31, 14, 15, 16, 7, 81, 19]
arr5 = [91, 81, 71, 16, 5, 114, 3, 21, 11, 0]
arr6 = []
for x in range(0, 10):
    x = arr4[x]+arr5[x]
    arr6.append(x)
print(arr6)
arrlen2 = len(arr6)
print(arrlen2)
