# 고급정렬: 4.Merge Sort: 2025.9.19 최정훈 길이 43줄 
def mergeSort(A, p:int, r:int, depth:int):
	if p < r:
		q = (p+r) // 2
		printSpace(depth)    # recursion의 depth*4칸만큼 들여쓰기
		print("mergeSort(", p, ",", q, ") and mergeSort(", q+1, ",", r, ")")   # 좌우분할해 2번 재귀호출
		mergeSort(A, p, q, depth+1)
		mergeSort(A, q+1, r, depth+1)
		printSpace(depth)
		print("merge(", p, ",", q, ",", r,")") #
		merge(A, p, q, r)
		##printSpace(depth)		# merge() 호출 후의 결과 출력
		print("merged A[]:", A)

def merge(A, p:int, q:int, r:int):
	i = p; j = q+1; t = 0
	tmp = [0 for i in range(len(A))]
	while i <= q and j <= r:
		if A[i] <= A[j]:
			tmp[t] = A[i]; t += 1; i += 1
		else:
			tmp[t] = A[j]; t += 1; j += 1
	while i <= q:
		tmp[t] = A[i]; t += 1; i += 1
	while j <= r:
		tmp[t] = A[j]; t += 1; j += 1
	i = p; t = 0
	while i <= r:
		A[i] = tmp[t]; t += 1; i += 1

def printSpace(depth:int):
	i = 0
	while (i <= depth):  # recursion의 depth만큼 들여쓰기
		print("    ", end="")
		i = i+1

if __name__ == "__main__":
    A = [31, 3, 65, 73, 8, 11, 20, 29, 48, 15]  # 교재 107p
    print("A[]       :", A)
    depth = 0     # recusion 깊이를 표시하기 위한 변수
    print("mergeSort(", 0, ",", len(A)-1, ")") 
    mergeSort(A, 0, len(A)-1, depth)
    print("Sorted A[]:", A)