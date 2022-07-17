numbers=[]
len(numbers) #리스트의 길이
print(len(numbers))

numbers.append(5)#리스트의 값 추가 (무조건 오른쪽)
numbers.append(8)
print(numbers)
print(len(numbers))

numbers2=[2,3,5,7,11,13,17,19]
del numbers2[3]#인덱스의 요소를 지움
print(numbers2)
numbers2.insert(4, 37)#인덱스의 요소 삽입 4번 인덱스 자리에 37을 추가 (원하는 위치)
print(numbers2)