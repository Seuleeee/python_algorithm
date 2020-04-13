# 백준 10818번 최소,최대
import sys
t = int(sys.stdin.readline())
number_ls = []
number_ls = list(map(int, sys.stdin.readline().split()))
number_ls.sort()
print("{} {}".format(int(number_ls[0]), int(number_ls[len(number_ls)-1])))