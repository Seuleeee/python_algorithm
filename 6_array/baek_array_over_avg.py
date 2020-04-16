# 백준 4344번
t = int(input())
for i in range(t):
    score_ls = list(map(int, input().split()))
    student_num = score_ls[0]
    sum_score = sum(score_ls[1:])
    avg = sum_score/student_num
    cnt = 0
    for data in score_ls[1:]:
        if data > avg:
            cnt += 1
    print(format(cnt/student_num*100, ".3f")+"%")