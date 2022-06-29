#: 1일 될때까지 예제의 시간복잡도, 공간 복잡도를 분석한다.
import time
import os 
import psutil 
process=psutil.Process(os.getpid())
start_time=time.time()


#n,k=map(int,input('두 수를 공백으로 분리하여 입력하시오>').split()) # N, K을 공백을 기준으로 구분하여 입력 받기
n=25
k=4
result = 0
while True: # 반복 루프 시작
    target =(n//k)*k 
# K로 나누어 지는 수를 구함, 예) 25 나누기 4 곱하기 4 = 처음 24
    result += (n - target) # N이 K로 나누어 떨어지는 수가 될 때까지 빼기, 1
    n = target # 25를 24로 수정
    if n < k: # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        break
    result += 1 # 횟수 증가
    n //= k # K로 나누기, n = 6
result += (n - 1) # 마지막으로 남은 수에 대하여 1씩 빼기, 6, 5 --> 4일때까지 2번 추가 빼기, 마지막 1번 나누고
print("1이 도달하기 까지 연산 횟수 :", result) # 총 5번 횟수 연산


end_time=time.time() 
print("time:",format(end_time-start_time,'.10f'))
print('MB bytes:',process.memory_info().rss/(1024.0*1024.0))
