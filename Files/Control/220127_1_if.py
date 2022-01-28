"""
Date : 22.01.27
Title : if문
Project : 
Name : 박상현
"""
T = True
if T:  # if(T) = if T:
    print("T는")  # Python의 if문은 { }를 들여쓰기 "    "로 구분한다
    print("True입니다.")
    #   print("Error!") 들여쓰기 2번은 Error!
else:
    print("Dead code")

T1 = True
T2 = True
if T1 and T2:  # or, not
    print("T1과 T2 모두 True 입니다")

list = [1, 2, 3]
if 1 in list: #in, not in
    print("list안에 1이 있습니다")

F = False
if F:
    print("거짓!")
else:
    pass #무시한다

F1 = F2 = False
if F1:
    print("F!")
elif F2: #else if
    print("F2")
elif T:
    print("T")

print("TURE!") if T else print("False!")
# if T:
#     print("TURE!")
# else:
#     print("False!")