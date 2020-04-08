# 백준 1110번 더하기 사이클
import sys
number = int(sys.stdin.readline())
n = number
cnt = 0
while True:
     cnt += 1
     n = (n % 10)*10 + ((n//10)+(n % 10))%10
     if n == number:
         break
print(cnt)