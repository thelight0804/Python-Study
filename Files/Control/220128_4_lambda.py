"""
Date : 22.01.28
Title : lambda (람다)
Project :
Name : 박상현
"""
#lambda : 한 줄로 만드는 간단한 함수
sum = lambda a, b: a+b
sub = lambda a, b: a-b

num1 = sum(5, 10)
num2 = sub(5, 10)

print("sum :", num1)
print("sub :", num2)

def sum(a, b):
    return a+b

def sub(a, b):
    return a-b