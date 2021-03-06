# 백준 2884번
# 알람 45분 일찍 설정하기
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

while True:
    H, M = map(int, input().split())
    if H>=0 and H<=23 and M>=0 and M<=59:
        break
    else:
        print("시간은 0~23, 분은 0~59의 정수로 입력가능합니다.")

# 1. H가 0이아니고 M에서 45를 뺐을 때 시간도 빼야하는 경우
if H != 0 and (M-45) < 0:
    print("{} {}".format(H-1, 60-(45-M)))
# 2. H가 0이고 M에서 45를 뺐을 때 시간도 빼야하는 경우
elif H == 0 and (M-45) < 0:
    print("{} {}".format(23, 60-(45-M)))
# 3. M에서 45만 빼면되는 경우
else:
    print("{} {}".format(H, M-45))
