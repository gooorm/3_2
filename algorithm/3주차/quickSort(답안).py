# 고급정렬: 5.Quick Sort: 2025.9.19 최정훈 길이 37줄 
#            (depth로 recusion 깊이 표시)
def quickSort(A, p:int, r:int, depth:int):
	if p < r:
		q = partition(A, p, r)	 # 분할
		printSpace(depth)
		print(q, "= partition(", p, ",", r, ")") #
		##printSpace(depth)
		print("partitioned A[]:", A)
		printSpace(depth)    # recursion의 depth*4칸만큼 들여쓰기
		print("quickSort(", p, ",", q-1, ") and quickSort(", q+1, ",", r, ")")   # 좌우분할해 2번 재귀호출
		quickSort(A, p, q-1, depth+1)	 # 왼쪽 부분 리스트 정렬
		quickSort(A, q+1, r, depth+1)	 # 오른쪽 부분 리스트 정렬

def partition(A, p:int, r:int) -> int:
	x = A[r]					# x: 기준 원소
	i = p-1					# i: 1구역의 끝 지점
	for j in range(p, r):	# j: 3구역의 시작 지점
		if A[j] < x:
			i += 1
			A[i], A[j] = A[j], A[i]  # 교환
	A[i+1], A[r] = A[r], A[i+1]	   # 기준 원소와 2구역 첫 원소 교환
	return i+1

def printSpace(depth:int):
	i = 0
	while (i <= depth):  # recursion의 depth*4만큼 들여쓰기
		print("    ", end="")
		i = i+1

if __name__ == "__main__":
    A = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]  # 교재 115p
    print("A[]            :", A)
    depth = 0     # recusion 깊이를 표시하기 위한 변수
    print("quickSort(", 0, ",", len(A)-1, ")") 
    quickSort(A, 0, len(A)-1, depth)
    print("Sorted A[]     :", A)