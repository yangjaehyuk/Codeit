alphabet_list=['A','B','C','D','E','F','G','H','I','J'] #리스트

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

alphabet_string='ABCDEFGHIJ' #문자열

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

alphabet_list=['A','B','C','D','E','F','G','H','I','J'] #리스트 슬라이싱

print(alphabet_list[0:5]) #인덱스 0부터 인덱스 4까지
print(alphabet_list[4:]) #인덱스 4부터 끝까지
print(alphabet_list[:4]) #맨앞(인덱스0)부터 인덱스3까지

alphabet_string='ABCDEFGHIJ' #문자열 슬라이싱 (새로운 문자열이 만들어짐)

print(alphabet_string[0:5]) #인덱스 0부터 인덱스 4까지
print(alphabet_string[4:]) #인덱스 4부터 끝까지
print(alphabet_string[:4]) #맨앞(인덱스0)부터 인덱스3까지

str_1='Hello'
str_2='World'
str_3=str_1+str_2
print(str_3)

list_1=[1,2,3,4]
list_2=[5,6,7,8]
list_3=list_1+list_2
print(list_3)

my_list=[2,3,5,7,11]
print(len(my_list)) #len: 리스트에 몇개의 요소가있는지 확인

my_string='Hello world!'
print(len(my_string)) #len: 문자열의 길이 (띄어쓰기와 느낌표 포함)

numbers=[1,2,3,4]
numbers[0]=5
print(numbers)

name='codeit' #문자열은 리스트와 달리 수정이 불가능함 하지만 name='codeit'+'it'과 같이 더하는 것은 아무 문제없이 실행 가능
name[0]='C'
print(name)