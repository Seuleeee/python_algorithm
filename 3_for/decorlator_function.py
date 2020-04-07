# ID와 Password가 확인한 후 함수가 동작하도록 만들기
import random
datas = [
    {"id":"Kobe", "pwd":"Bryant", "addr":"LA"},
    {"id":"Michael", "pwd":"Jordan", "addr":"Chicago"},
    {"id":"Shaquile", "pwd":"O'Neal", "addr":"LA"},
    {"id":"Kevin", "pwd":"Durant", "addr":"Brooklyn"}
]

def check_func(func):
    """
    check id and password
    :param func: function
    :return: wrapper
    """

    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: result of implementing the function
        """
        input_id = input("insert ID : ")
        input_pwd = input("insert Password : ")
        result = 0;
        for data in datas:
            if data["id"] == input_id and data["pwd"] == input_pwd:
                result = func(*args, **kwargs)
                return result
        print("일치하는 정보가 없습니다.")
    return wrapper

@check_func
def plus(a, b):
    return a+b

@check_func
def get_lotto_number():
    """
    make and get lotto number
    :return:
    """
    #번호를 담을 리스트를 만든다.
    number_ls = []
    while True:
         number = random.randint(1, 45)
         if number not in number_ls:
             number_ls.append(number)
         if len(number_ls) >= 6:
             number_ls.sort()
             break
    print(number_ls)

plus_result = plus(3,4)
print(plus_result)
get_lotto_number()

