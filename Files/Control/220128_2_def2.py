"""
Date : 22.01.28
Title : 함수(유동 매개변수)
Project : 1부터 입력받은 숫자까지 더하기
Name : 박상현
"""


def add_many(choice, *n):
    result = 1 #곱셈을 이용하기 위해 1로 지정
    if choice == "add":
        for i in n:
            result += i
        return result-1 #1부터 더했기 때문에 -1을 해준다
    elif choice == "mul":
        for i in n:
            result *= i
        return result

###

num = add_many("add", 1, 2, 3, 4, 5)
print("1~5 sum :", num)

num = add_many("mul", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("1~10 mul :", num)