
arr = [1, 5, 10, 13, 24, 0, 98, 134, 5, 7]

setarr = set(arr)
if len(arr) == len(setarr):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые")