numbers=[19,13,2,5,3,11,7,17]

new_list=sorted(numbers) #작은것부터 정렬
print(new_list)

new_list=sorted(numbers,reverse=True) #큰것부터 정렬
print(new_list)

#sorted는 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴

print(numbers.sort()) #sort는 아무것도 return하지 않지만 기존 리스트를 정렬

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)