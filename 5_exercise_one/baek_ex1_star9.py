# 백준 2523번 별찍기
import sys
t = int(sys.stdin.readline())
for i in range(1, t*2):
    if i <= t:
        print(" "*(i-1)+"*" * ((t-i)*2+1))
    else:
        print(" " * (t*2-i-1) + "*" * ((i-t) * 2 + 1))