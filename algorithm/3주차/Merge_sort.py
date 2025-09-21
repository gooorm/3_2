import random

def mergeSort(p, r, arr):

    if p < r:
        q = int((p + r) / 2)
        mergeSort(p, q, arr)
        mergeSort(q + 1, r, arr)
        merge(p, q + 1, r, arr)


def merge(p, q, r, arr):
    list1 = arr[p:q + 1]
    list2 = arr[q + 1:r + 1]

    merged_list = []
    print(a, b)
    # for i in range(r):
    #     if list
    #




    print(p, q, r, merged_list)
    for x in range(p, r):
        #print(x, p)
        arr[x] = merged_list[x - p]
    merged_list

max_size = 10

M = [random.randint(0, 100) for _ in range(max_size)]

print(M)
mergeSort(0, max_size - 1, M)
print(M)
