# 기본정렬: 3.Insertion Sort: 2025.9.12 최정훈 길이 17줄 
def insertionSort(A):
	for i in range(1, len(A)):
		newItem = A[i]
		j = i - 1
		while j >= 0 and newItem < A[j]:
			A[j + 1] = A[j]
			j -= 1
		A[j+1] = newItem
		print("[#", i, "] new", newItem, A)

# Example usage:
if __name__ == "__main__":
    A = [3, 40, 32, 38, 8, 11, 50, 39, 65, 15]    #교재 102p
    print("A[]:	   ", A)
    insertionSort(A)
    print("Sorted A[]:", A)