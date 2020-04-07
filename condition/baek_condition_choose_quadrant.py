# 백준 14681번
# 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
# Quadrant n은 제 n 사분면이라는 뜻

while True:
    x = int(input())
    y = int(input())

    if x >= -1000 and x <=1000 and x != 0 and y >= -1000 and y <=1000 and y != 0 :
        break
    else:
        print("-1000보다 크고 1000보다 작으며 0이 아닌 정수를 입력하세요.")
# 제 1사분면
if x>0 and y>0:
    print(1)
# 제 2사분면
elif x<0 and y>0:
    print(2)
# 제 3사분면
elif x<0 and y<0:
    print(3)
# 제 4사분면
elif x>0 and y<0:
    print(4)