#백준 1065번
num = int(input())
cnt = 0
for i in range(1, num+1):
    if i < 100:
        cnt += 1
        continue
    nums = list(map(int, str(i)))
    if nums[1] - nums[0] == nums[2] - nums[1]:
        cnt += 1
print(cnt)

