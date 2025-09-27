# 고급정렬: 6.Shell Sort: 2025.9.26 최정훈 길이 38줄 
def shellSort(A):  # A[0...n-1]: 정렬할 리스트
	H = gapSequence(len(A)-1)
	print("===============Shell Sort Demo by CJH==================================")
	for h in H:  # H = [h0, h1, ..., 1]: 
		for k in range(h):
			print("stepInsertionSort(A, ", k, ", ", h,") -----", sep="")
			stepInsertionSort(A, k, h)
			print("           ",A, "<-----", k, h)
		print("=========================================================")	

def stepInsertionSort(A, k:int, h:int):  # A[k, k+h, k+2h, ...]을 정렬한다
	for i in range(k + h, len(A), h):
		j = i - h
		newItem = A[i]
		print("[#", i, "] new", newItem)
		# 이 지점에서 A[..., j-2h, j-h, j]는 이미 정렬되어 있는 상태임
		# A[..., j-2h, j-h, j, j+h]의 맞는 곳에 A[j+h]를 삽입한다
		while 0 <= j and newItem < A[j]:
			A[j + h] = A[j]
			j -= h
		A[j + h] = newItem	

def gapSequence(n:int) -> list: # 갭 수열 만들기. 다양한 선택이 있음
	H = [1]; gap = 1          
	k = 2					
	while gap < n/2:		#갭 수열   ... 31, 15, 7, 3, 1
		gap = 2 ** k - 1
		H.append(gap)
		k += 1
	H.reverse()
	print("Gap Sequence = ", H, "**********")
	return H

if __name__ == "__main__":
    A = [15, 31, 65, 73, 8, 66, 11, 3, 20, 48, 29, 1, 33, 25, 4]    #교재 140p
    print("A[]:       ", A)
    shellSort(A)
    print("Sorted A[]:", A)