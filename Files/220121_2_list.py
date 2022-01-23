list = [0, 1, 2, ['A', 'B', 'C']]
print("list[0] = " , list[0]) #포매팅 대신 ' , '로 print 가능
print("list[-1] = ", list[-1]) #list안에 list를 넣을 수 있다
print("list[-1][1] = ", list[-1][1])
print("list[0:2] = ", list[0:2])

print("*"*10)
#list 연산
list1 = [3, 4, 5]
list2 = ["D", "E", "F"]
print("list1 + list2 = ", list1 + list2) 
print("list2 * 3 = ", list2 * 3)
print("len(list1) = ", len(list1)) #

print("*"*10)
#list 수정과 삭제
list3 = [6, 7, 8]
list3[0] = "A" #수정
print("replace) list3 = ", list3)

del list3[0] #삭제
print("del) list3 = ", list3)

print("*"*10)
#list 함수
list4 = [1,2,3]
list4.append(0) #추가 (마지막)
print(".append) list4 = ", list4)

list4.insert(2, 10)
print(".insert) list4 = ", list4)

list4.sort() #오름차순 변경 / 숫자와 문자가 같이 있으면 오류!
print(".sort) list4 = ", list4)

print("list4.index(1) = ", list4.index(1)) #위치 반환
print("list4.count(0) = ", list4.count(0)) #0 개수 반환