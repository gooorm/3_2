# 2반 - 특수정렬: 8.Radix Sort: 2025.9.26 최정훈 길이 22줄 
import math

def radixSort(A):
	maxValue = max(A)
	numDigits = math.ceil(math.log10(maxValue))  # 자릿수 계산
	bucket = [[] for _ in range(10)]  # 0, 1, ..., 9에 대한 10개의 리스트
	for i in range(numDigits):
        # 
		#i번째 자릿수에 대해 A[0..n-1]을 안정성을 유지하면서 정렬토록 코드를 완성하시오
        #  
		#print(f"End of pass for digit {i}, A: {A} --------")

if __name__ == "__main__":
    print("Radix Sort test **********************************")
    A = [123, 2154, 222, 4, 283, 1560, 1061, 2150]
    print("A[]:       ", A)
    radixSort(A)
    print("Sorted A[]:", A)