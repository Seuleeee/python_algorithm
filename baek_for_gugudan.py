#백준 2739번 구구단

while True:
    dan = int(input())

    if dan > 1 and dan < 10:
        break
    else:
        print("2부터 9까지 정수를 입력하세요.")


for data in range(1,10):
    print("{} * {} = {}".format(dan, data, dan* data))
