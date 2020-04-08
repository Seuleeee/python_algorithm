# 백준 2741번 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
import sys
T = int(sys.stdin.readline())
for data in range(T, 0, -1): #최초값, 최종값, 증감폭
    print(data)