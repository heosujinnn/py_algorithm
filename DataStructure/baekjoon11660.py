'''
구간 합: 합 배열을 이용하여 시간복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘.
S[4]=A[0]+A[1]+...+A[4]

합 배열을 만든 방법 : S[i]=S[i-1]+A[i]
구간 합을 구하는 공식 : S[j]-S[i-1]  (i에서 j까지의 구간합)
'''
# 구간 합 구하기 백준 11660번 
# 이차원 배열 N*N 
# D[i][j]의 합 공식: D[i][j-1]+D[i-1][j]-D[i-1][Dj-1]+A[i][j]
# 구간합으로 구하는 법: D[x2y2]-D[x1-1][y2]-D[x2][Y1-1]+D[x1-1][y1-1]
#           2 2 3 4 = D[3][4]-D[1][4]-D[3][1]+D[1][1]
'''
예시: 
4 3      => 이차원배열의 크기, 구간 합 질의의 개수
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

2 2 3 4  => 27
3 4 3 4  => 6
1 1 4 4  => 64
'''
'''원본 데이터 저장해주고 합배열 저장하고 질의에 대한 결과 계산하고 출력한다. (n리스트크기,m질의의수,A원본리스트,D합배열)'''
import sys 
input=sys.stdin.readline

n,m=map(int, input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row=[0]+[int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j]=D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]

for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    res=D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]
    print(res)


