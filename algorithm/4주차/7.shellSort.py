# 2반 - 고급정렬: 7.Shell Sort: 2025.9.26 최정훈 길이 33줄 
# 주어진 gapSequence를 이용해 stepInsertion 및 shellSort를 완성하시요
def shellSort(A):  # A[0...n-1]: 정렬할 리스트
    H = gapSequence(len(A)-1)


def stepInsertionSort(A, k:int, h:int):  # A[k, k+h, k+2h, ...]을 정렬한다



def gapSequence(n:int) -> list: # 갭 수열 만들기. 다양한 선택이 있음
    H = [1]; gap = 1;
    k = 2
    while gap < n/2:
        gap = 2 ** k - 1
        H.append(gap)
        k += 1
    H.reverse()
    print("gapSequence = ", H)
    return H

if __name__ == "__main__":
    A = [15, 31, 65, 73, 8, 66, 11, 3, 20, 48, 29, 1, 33, 25, 4]    #교재 140p
    print("A[]:       ", A)
    shellSort(A)
    print("Sorted A[]:", A)