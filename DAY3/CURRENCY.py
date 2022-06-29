#그리디-거스름 돈 
#문제 : 음식점의 계산을 돕는 점원이 있다. 거슬러 주어야 할돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요. 
n=int(input("거스름돈을 가격 (정수)로 입력해주세요>"))
count=0

array=[500,100,50,10]
for coin in array: 
    count+=n//coin  #화폐로 거슬러 줄 수 있는 동전의 개수 세기 
    n%=coin 
print("동전의 거스름돈 최소 개수는 :",count) 

#시간,공간 복잡도 
import time
import os 
import psutil 
process=psutil.Process(os.getpid())
start_time=time.time()
n=1260 
array=[500,100,50,10]
for coin in array:
    count += n//coin 
print('동전의 거스름돈 최소개수 : ',count)
end_time=time.time() 
print("time:",format(end_time-start_time,'.10f'))
print('MB bytes:',process.memory_info().rss/(1024.0*1024.0))











