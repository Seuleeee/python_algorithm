# 백준 5543번 상근날드
import sys
burger_ls = []
beverage_ls = []
for i in range(1, 4):
    burger_ls.append(int(sys.stdin.readline()))
for i in range(1, 3):
    beverage_ls.append(int(sys.stdin.readline()))
burger_ls.sort()
beverage_ls.sort()
set_price = burger_ls[len(burger_ls)-1]+beverage_ls[len(beverage_ls)-1]
for i in burger_ls:
    for j in beverage_ls:
        if i+j < set_price:
            set_price = i+j
print(set_price - 50)