#백준 4673번
#1. 생성자를 만드는 수열 만들기

def make_d(a):
    num = str(a)
    sum = a
    for i in range(len(num)):
        sum += int(num[i])

    return sum
print(make_d(1))
self_num_ls = []
for i in range(1, 10000):
    result = make_d(i)
    if i == result:
        self_num_ls.append(i)
print(self_num_ls)
