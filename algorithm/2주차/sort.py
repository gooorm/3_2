def theLargest(arr):
    largest = arr.index(max(arr))
    return largest

def selectionSort(arr: list) -> None:
    for i in range(len(arr) - 1, 0, -1):
        largest_index =  theLargest(arr[:i + 1])
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        #print(arr)

def bubbleSort(arr: list):
    sorted = True
    for i in range(len(arr) - 1, 1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
            #print(arr)
    if sorted:
        return

def insertionSort(arr: list):
    for i in range(1, len(arr)):
        newItem = arr[i]
        for a in arr[:i]:
            if a > newItem:
                arr = arr[:arr.index(a)] + [newItem] + arr[arr.index(a):i]  + arr[i + 1:]
                break
        #print(arr)


def print_sort(arr: list, title: str, sortFunc):
    print('-' * 16 + f"{title}Sorting" + '-' * 16)
    print("arr: ", arr)
    sortFunc(arr)
    print("sorted arr: ", arr)
    print()

a = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
b = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
c = [3, 31, 48, 73, 8, 11, 50, 39, 65, 15]

print_sort(a, "Selection", selectionSort)
print_sort(b, "Bubble", bubbleSort)
print_sort(c, "Insert", insertionSort)