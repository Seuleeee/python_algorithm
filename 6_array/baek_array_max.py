# 백준 2562번
number_ls = []
for i in range(9):
    number_ls.append(int(input()))
max_num = max(number_ls)
print(max_num)
print(number_ls.index(max_num)+1)