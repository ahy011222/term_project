

# 6.15
# 연결 리스트 클래스 LinkedList(코드 6.5)에 merge() 연산을 구현하라. 연결 리스트 A와
# B가 있을때, A.merge(B)는 연결 리스트 A의 맨 뒤에 B를 추가하는 연산이다. 연산 결과
# A의 길이는 늘어나고, B의 길이는 0이 되도록 하라.


def merge(self, B):
    if B.head is not None: # B에 head가 None이 아니면
        n = self.head # 임의의 n이 self의 head를 가리킴
        while n.link is not None: # n의 link가 None이 아닐 때까지 반복 ( 즉, 최종적으로 n은 마지막 노드의 링크를 가지고 있음 )
            n = n.link # n의 연결리스트에 있는 마지막 노드까지 가기 위해 링크를 게속함
        n.link = B.head # n의 링크는 B 연결리스트의 head를 가리킴 ( 맨 뒤에 추가랑 같음 )
        B.head = None # 그리고 B의 head는 None이 되면서 크기가 0