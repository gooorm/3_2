# 특수정렬: 8.Radix Sort: 2025.9.26 최정훈 길이 22줄 
import math

def radixSort(A):
	maxValue = max(A)
	numDigits = math.ceil(math.log10(maxValue))  # 자릿수 계산
	bucket = [[] for _ in range(10)]  # 0, 1, ..., 9에 대한 10개의 리스트
	for i in range(numDigits):
		for x in A:
			y = (x // 10**i) % 10
			bucket[y].append(x)
		A.clear()
		for j in range(10):
			A.extend(bucket[j])
			bucket[j].clear()

if __name__ == "__main__":
    print("Radix Sort test")
    A = [123, 2154, 222, 4, 283, 1560, 1061, 2150]     # 교재 147p
    print("A[]:       ", A)
    radixSort(A)
    print("Sorted A[]:", A)