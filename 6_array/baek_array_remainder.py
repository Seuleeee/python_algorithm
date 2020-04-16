# 백준 3052번 나머지

num_ls = []
remain_ls = []
for i in range(10):
    num_ls.append(int(input()))

for data in num_ls:
    if data%42 not in remain_ls:
        remain_ls.append(data%42)

print(len(remain_ls))