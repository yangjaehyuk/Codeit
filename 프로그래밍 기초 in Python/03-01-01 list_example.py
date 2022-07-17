# 리스트(list)
numbers=[2,3,5,7,11,13]
names=["윤수","혜린","태호","영훈"]

print(numbers)
print(names)

#인덱싱(indexing)
print(names[1])
print(numbers[1]+numbers[3])
#print(numbers[6]) 오류 : 인덱스 범위 벗어남
print(numbers[-1])
print(numbers[-2])
#print(numbers[-7]) 오류

#리스트 슬라이싱
numbers[0:4] #리스트의 인덱스0부터 인덱스3까지 자름
print(numbers[0:4])
print(numbers[2:]) #인덱스 2부터 마지막 인덱스까지 가지고 있음
print(numbers[:3]) #맨앞부터 인덱스 2까지의 요소가 들어감

new_list=numbers[:3]
print(new_list[2])

numbers[0]=7
print(numbers)

numbers[0]=numbers[0]+numbers[1]
print(numbers)