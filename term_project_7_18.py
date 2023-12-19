

# 7.18
# 정렬된 리스트로 집합을 구현하는 경우 원소의 포함 여부를 검사하는 contains() 연산을
# 보다 효율적으로 처리할 수 있다. 코드 3.6의 ArraySet의 원소들이 7.3절과 같이 오름차순
# 으로 정렬되어 있다고 가정하고, 개선된 contains() 연산을 구현해 보라. 이진 탐색을 사
# 용할 수 있을 것이다.


def contains(self, e):
        low = 0 # 0번째 인덱스
        high = self.capacity-1 # self의 마지막 인덱스
        middle = (low + high)//2 # 중앙 위치 계산
        
        while(low <= high): # 반복 구조를 이용
            if (e == self[middle]): # middle값과 e(원소)값이 같으면 ( 원소가 포함 되어있다는 뜻 )
                return True # True 반환
            elif (e > self[middle]): # e(원소)값이 middle값보다 크면 low 값을 증가
                low = middle + 1
            else: # e(원소)값이 middle값보다 작으면 high값을 감소
                high = middle - 1
        return False # 원소가 포함 되어 있지 않으면 False 반환