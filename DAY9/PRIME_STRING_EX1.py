# 에라토스테네스의 체 적용 
#다시 해보기
#배수 제거 시킴 
import math 
def is_prime_number(n):
    li=[1]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        if li[i]:
            for j in range(i+i,n+1,i):
                li[j]=0
    p=[i for i in range(2,n+1)if li[i]]
    return p
while 1:
    s=input() 
    max_string=[] 
    if s=='0':
        break 
    p=is_prime_number(100000)
    res=2 
    for n in p:
        if str(n) in s: 
            res=n 
            max_string.append(res)
    print(max_string)
    print(max(max_string))
    
    ''' 
    내가 짠 코드 : (오류남)
import math

while True: 
    a=input()
    if a=='0':
        break 
	
n = 1000
array = [True for i in range(n + 1)]
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
	if array[i] == True: # i가 소수인 경우(남은 수인 경우)
# i를 제외한 i의 모든 배수를 지우기
		j = 2
		while i * j <= n:
			array[i * j] = False
			j += 1

#for i in range(2, n + 1):
	#if array[i]:
		#print(i, end='')
        
result=1
for x in array:
    if str(x)in a:
    	result=x
print(result)
  '''