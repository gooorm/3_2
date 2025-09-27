# 2반 - 특수정렬: 10.Bucket Sort: 2025.9.26 최정훈 길이 19줄 
import math
from insertionSort import insertionSort

def bucketSort(A):  # [0, 1) 범위의 실수 정렬
    n = len(A)

if __name__ == "__main__":
    A = [0.38, .94, .48, .73, .99, .43, .55, .15, .85, .84, .81, .71, .17, .10, .02]   # 교재 153p
    print("A[]:       ", A)
    bucketSort(A)
    print("Sorted A[]:", A)