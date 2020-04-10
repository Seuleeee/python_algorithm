# 백준 2523번 별찍기
import sys
t = int(sys.stdin.readline())
for i in range(1, t*2):
    if i > t:
        print("*" * (t*2-i))
    else:
        print("*" * i)