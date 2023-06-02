'''
나머지 합 구하기
N개의 수가 주어졌을 때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수를 구하시오.
즉 Ai~Aj까지의 합이 M으로 나누어 떨어지는 (i,j)쌍의 개수

1<=N<=10의 6승, 
2<=M<=10의 3승 

5(N) 3(M)
1 2 3 1 2   => 7

12,123,12312,231,3,312,12 (7가지)
문제 분석: 10의 6승: 1초안에 연산 어려워.
1(첫번째수)를 M인 3으로 나누어 떨어지는지 계산하고 한 칸씩 늘려가면서 계산해봐!!
그러면 1초에 연산은 불가능! 시간 복잡도 줄이기 위해서 어떻게 하냐??
(A+b)%c 는 ((A%C)+(B%C))%C 와 같다. 
'''
#1. 리스트를 합배열로 만든다. 
#2. 합배열의 모든 값을 M으로 나눈 나머지 연산을 한다.
#3. 변경된 내용에서 0인 부분은 원본리스트에서 구간합이 이미 M으로 나누어 떨어진다. 
#4. 
import sys
input=sys.stdin.readline
n,m=map(int, input().split())
A=list(map(int,input().split()))
S=[0]*n
C=[0]*m 
answer=0

S[0]=A[0]
for i in range(1,n):
    S[i]=S[i-1]+A[i]
for i in range(n):
    remainder=S[i]%m 
    if remainder==0:
        answer+=1 
    C[remainder]+=1 #1이되면1을 추가하기

for i in range(m):
    if C[i]>1 : #같은 나머지 값을 가진애가 2개 이상 있다면
      answer+=(C[i]*(C[i]-1)//2) # nCm => 조합공식 
print(answer)



