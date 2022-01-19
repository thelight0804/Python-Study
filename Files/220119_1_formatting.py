"""
Date : 22.01.19
Title : 문자열 포매팅
Project : 
Name : 박상현
"""
# 숫자 대입 (%d)
hour = 15
str = "지금은 %d시 %d분 입니다" % (hour, 18)
print(str)

# 문자열 대입 (%s)
str = "1시간마다 %s을 해주어야 합니다" % "스트레칭"
print(str)

# %s 포맷 코드
str = "%%s 포맷 코드는 정수(%s)든 실수(%s)든 모두 문자열로 변환해요" % (3, 3.15) #%% : % 표시
print(str)

#숫자 포맷 코드
str = "%%5d = %5d" % 5 #Nd = N칸 사용 (음수도 가능)
print(str)

str = "%%0.3f = %0.3f" % 3.141592 #0.Nf = N만큼의 소수점 (반올림)
print(str)

str = "%%8.3f = %8.4f" % 3.141592 #3.1415를 8칸 사용
print(str)


print('*'*10)
#format 함수를 사용한 포매팅
function = "Bluetooth"
num = 3
str = "현재 {0}에 {1}개의 기기가 연결되어 있습니다.".format(function, num)
print(str)

#이름으로 포매팅
function = "Wi-Fi"
num = 4
str = "{{ {0} }} 검색 기기 수 : {num}".format(function, num=4)
#{{  }} = "{ }" 표기
print(str)

print('*'*10)
#f"" 문자열 포매팅 (3.6 이상 가능)
acquire = "Microsoft"
company = "Blizzard"
money = 82
print(f"{acquire}는 {company}을 {money}조원에 인수 했습니다.")