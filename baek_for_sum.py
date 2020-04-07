# 백준 8393번 n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

while True:
    num = int(input())
    if num>=1 and num <=10000:
        break
    else:
        print("1부터 10000까지의 정수를 입력하세요.")
sum=0
for i in range(1,num+1):
    sum += i

print(sum)