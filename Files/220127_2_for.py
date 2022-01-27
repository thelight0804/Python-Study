"""
Date : 22.01.27
Title : if문
Project : 
Name : 박상현
"""
t1 = ("1. Galaxy", "2. iPhone", "3. Pixel")
for i in t1[:2]: #t1의 2개만 반환
    print(i)
    print(type(t1))

#홀수만 합하여 평균
import random
num = [] # tuple은 개수 변경이 안 되니 list로

for i in range(10): #난수 생성
    temp = random.randrange(1, 500)
    num.append(temp)
print("num : ", num)

sum = 0
for i in range(len(num)): #num의 길이만큼 반복
    if num[i] %2 == 0:
        sum += num[i]
avg = sum/len(num)
print("avg = ", avg)