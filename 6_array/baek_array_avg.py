# 백준 1546번
t = int(input())
score_ls = list(map(int, input().split()))
new_score_ls = []
m = max(score_ls)
total = 0
for data in score_ls:
    new_score_ls.append(data/m*100)
for data in new_score_ls:
    total += data
avg = total/t
print(avg)
