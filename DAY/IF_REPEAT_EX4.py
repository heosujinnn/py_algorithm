#문제 1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
# for, while 문 선택

a=int(input("정수입력>"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        
        sum+=i
        
print(sum)
        
# 문제2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
# While 문과 if문 활용

while True:
    a=str(input("문자 입력>"))
    if a=='q':
        break
        
    else:
        print(a)



