#mutable_object=[1,2,3]
#immutable_object=(1,2,3)

#mutable_object[0]=4
#print(mutable_object) #0번째 요소가 4로 바뀜

#immutable_object[0]=4
#print(immutable_object) #바뀌지 않음 에러난다

#tuple_x=(6,4)
#tuple_x[0]=4
#tuple_x[1]=1
#print(tuple_x) #에러 발생

#tuple_x=(6,4)
#tuple_x=(4,1)
#tuple_x=(4,1,7)
#print(tuple_x) #아예 새로운 인스턴스를 제공해주는 경우에는 출력이 됨 불변타입

list_x=[]
list_x.append(4)
list_x.append(1)
list_x.append(7)

print(list_x) #이미 생성된 객체의 속성을 바꿀 수 있다 가변타입(직접 작성하는 클래스는 가변타입 즉 인스턴스 변경 시 원래 인스턴스의 속성을 바꾸면 됨)