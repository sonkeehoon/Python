class LinkedListElement: # 노드
    def __init__(self, val, ptr):
        self.value = val
        self.myNext = ptr

node1 = LinkedListElement(10, None)
node2 = LinkedListElement(20, None)
node1.myNext = node2
node3 = LinkedListElement(30, None)
node2.myNext = node3

cur = node1 # 시작 노드
while cur.myNext is not None: # 다음 가리키는 노드가 없을 때 까지 반복합니다
    print(f"current value :", cur.value, "| next value :", cur.myNext.value) # 현재 값을 출력
    cur = cur.myNext # cur을 다음으로 가리키는(myNext) 노드로 갱신해줍니다
    
print("end value is", cur.value, "| next value :", cur.myNext)