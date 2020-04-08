# 백준 10871번 x보다 작은 수
import sys
n, x = map(int, sys.stdin.readline().split())
number_ls = list(map(int, sys.stdin.readline().split()))
for i in number_ls:
    if i < x:
        print(i, end=' ')
