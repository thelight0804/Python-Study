"""
Date : 22.01.21
Title : 튜플 (tuple)
Project : 
Name : 박상현
"""

t1 = (1, 2, 3)
t2 = (4, ) #1개의 요소를 가질 때는 콤마 ( , )를 붙어야 한다
t3 = 4, 
tA = "A", "B", "C"  # 괄호 '( )' 없이도 tuple을 만들 수 있다
print("t1 = ", t1, "\t tA = ", tA)

# del t1  # tuple 제거
# del tA[0] #tuple 요소를 제거/변경하지는 못한다

print("*"*10)
print("tA[0] = ", tA[0]) #인덱싱
print("tA[:2] = ", tA[:3]) #슬라이싱
print("t1 + tA = ", t1 + tA) #합치기 (덧셈)
print("tA * 3 = ", tA*3) #반복 (곱셈)
print("len(tA) = ", len(tA)) #길이 구하기