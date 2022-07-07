#문제 : N개의 수로 된 수열 A[1], A[2], ….A[N]이 있다.
#이 수열의 i번째수부터 J번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램을작성하시오.
n = int(input())
m = int(input())
data = list(map(int, input().split()))


count = 0
interval_sum = 0
end = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
# end를 가능한 만큼 이동시키기
	while interval_sum < m and end < n:
		interval_sum += data[end]
		end += 1
        
        # 부분합이 m일 때 카운트 증가
	if interval_sum == m:
		count += 1
	interval_sum -= data[start]
print(count)




