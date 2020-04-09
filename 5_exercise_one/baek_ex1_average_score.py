#백준 10039번 입력은 총 5줄로 이루어져 있고, 원섭이의 점수, 세희의 점수, 상근이의 점수, 숭이의 점수, 강수의 점수가 순서대로 주어진다.
# 점수는 모두 0점 이상, 100점 이하인 5의 배수이다. 따라서, 평균 점수는 항상 정수이다.

import sys
score_ls=[]
sum = 0
avg = 0
for data in range(1,6):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    score_ls.append(score)
for data in score_ls:
    sum += data
avg = int(sum/5)
print(avg)