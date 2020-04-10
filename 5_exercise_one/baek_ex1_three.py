#백준 10817 세 수 중 두번째로 큰 수 출력
import sys
a, b, c = map(int, sys.stdin.readline().split())
num_ls = [a, b, c]
num_ls.sort()
print(num_ls[1])