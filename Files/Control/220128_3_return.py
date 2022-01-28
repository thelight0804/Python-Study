"""
Date : 22.01.28
Title : 함수 return
Project :
Name : 박상현
"""
def two_returns():
    a = 5
    b = 10
    return a, b #return값이 여러 개 일때는 tuple로 반환한다

def fastfood(name, junk = True): #매개변수 초기화
    if junk == True:
        print("%s is fastfood." % name)
    else:
        print("%s is not fastfood." % name)

result = two_returns()
print(result)
print(type(result))

num1, num2 = two_returns() #각각의 return값을 따로 반환할 수 있다
print("num1 :", num1, " / num2 :", num2)

fastfood("pizza")
fastfood("sandwich", False) #junk = False