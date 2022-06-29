#2중 반복문을 이용하는 프로그램 예제, N = 2000 기준, 시간 계산
import time 
import random 

start_time=time.time()
array=[]
for v in range(2000):
    array.append(random.randint(0,10))
for i in array:
    for j in array:
        temp=i*j 
    
print(temp)
end_time=time.time()
print("time:",end_time-start_time)

