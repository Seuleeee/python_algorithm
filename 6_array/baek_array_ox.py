# 백준 8958번
t = int(input())
for i in range(t):
    str_ls = list(input())
    sum = 0
    score = 1
    for i in str_ls:
        if i == 'O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)