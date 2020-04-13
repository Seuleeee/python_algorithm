# 백준 10996번 별찍기
import sys
t = int(sys.stdin.readline())
if t == 1:
    print("*")
else:
    if t%2 == 1:
        a = "* " *(t//2)+"*"
        b = " *" * (t//2)
    else:
        a = "* " * (t//2)
        b = " *" * (t//2)

    for _ in range(1, t+1):
        print(a)
        print(b)
