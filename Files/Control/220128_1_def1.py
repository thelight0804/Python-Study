"""
Date : 22.01.28
Title : 함수
Project : 사칙연산 계산기
Name : 박상현
"""
def add(n, i): #함수 (앞쪽에 선언 해주어야 한다)
    return n+i

def sub(n, i):
    return n-i

def mul(n, i):
    return n*i

def div(n, i):
    return n/i

print("[사칙연산 계산기]")
a = int(input("첫 번째 숫자 : ")) #input () : 문자열로 입력을 받는다
b = int(input("두 번째 숫자 : "))

sum = add(a, b)
sub = sub(a, b) #변수 이름이 함수 이름과 일치해도 무관하다
mul = mul(i = b, n = a) #매개변수의 순서를 지정할 수 있다
div = div(a, b)

print("합계 : ", sum)
print("뺄셈 : ", sub)
print("곱셈 : ", mul)
print("나눗셈 : ", div)