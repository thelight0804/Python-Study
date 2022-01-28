"""
Date : 22.01.18
Title : 문자열 (String)
Project : 
Name : 박상현
"""

#한 줄 문자열

#('~') 사용
print('오늘 점심은 "돈까스"를 얹은 우동입니다')
print('이마트 트레이더스\'s 피자는 정말 맛있습니다')

# ("~") 사용
print("이마트 트레이더스's 피자는 정말 맛있습니다")
print("오늘 점심은 \"돈까스\"를 얹은 우동입니다")

 # 문자열 내에서 ( ', " )을 사용하기 위해 ""과 ''가 구분되어 있다
 # \' 또는 \" 을 사용하면 ""과 '' 구분없이 사용할 수 있다

#####################

#여러 줄 문자열
str = "\nC와 같이 \n\\n을 사용하여\n줄바꿈을 할 수 있어요\n"
print (str) #\\ : '\'을 표현할 때 사용

str = '''대신귀
여운오
타에를
드리겠
습니다
'''
print(str)

#####################

#문자열 연산

##문자열 덧셈 (연결)
a = "Hello"
b = ' world!'
print(a+b) #"~"와 '~'의 계산도 가능

##문자열 곱셈 (반복)
a = "*"
b = 5
print(a*b)

##문자열 길이
a = "I need you!"
b = "도레미파"
print("a의 길이 : ", len(a) )
print("b의 길이 : ",len(b) ) #한글의 글자 하나를 1로 계산한다
print("*"*10)

#문자열 Indexing
#Indexing : 가리킨다 (찾기)
a = "abcde"
print("a[3] : ", a[3]) #d
print("a[-1] : ", a[-1], "\ta[-2] : ", a[-2]) #-1 : 뒤에서부터 찾는다
print("a[0:5]", a[0:5]) #a[시작번호:끝번호]
print("a[0:] : ", a[0:]) #a[시작번호:] : 시작번호부터 끝까지
print("a[:5] : ", a[:5]) #a[:n] : 처음부터 n번까지
print("a[:]", a[:]) #a[:] : 처음부터 끝까지

print("*"*10)
#문자열 분리
now = "22011816:22대한민국창원시"
date = now[0:6]
time = now[6:11]
country = now[11:15]
city = now[-3:] #-3부터 끝까지
print("date = ", date)
print("time = ", time)
print("country = ", country)
print("city = ", city)