#퀵정렬 성능 
from random import randint
import time
# 배열에 10,000개의 정수를 삽입
array = []

for _ in range(10000):
# 1부터 100 사이의 랜덤한 정수
	array.append(randint(1, 100))
start_time = time.time()
    

def quick_sort(array):
# 리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array
	pivot = array[0] # 피벗은 첫 번째 원소
	tail = array[1:] # 피벗을 제외한 리스트
	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    
# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("퀵 정렬 성능 측정:", end_time - start_time)
