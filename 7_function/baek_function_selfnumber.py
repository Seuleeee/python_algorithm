#백준 4673번
#1. 생성자를 만드는 수열 만들기
#2. 생성자가 있나없나 판단하기
#3. 생성자 없는 것 가려내기
def make_d(a):
    num = str(a)
    sum = a
    for i in range(len(num)):
        sum += int(num[i])
    return sum
self_num_ls = []
for i in range(1, 10000):
    result = make_d(i)
    self_num_ls.append(result)
self_num = []
for i in range(1, 10000):
    if i not in self_num_ls:
        print(i)