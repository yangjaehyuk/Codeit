my_family={
    '엄마':'김자옥',
    '아빠':'이석진',
    '아들':'이동민',
    '딸':'이지영'
}
print(my_family.values())
print('이지영' in my_family.values()) #이지영은 존재하므로 True
print('성태호' in my_family.values()) #성태호는 존재하지 않으므로 False

for value in my_family.values():
    print(value)

print(my_family.keys())

for key in my_family.keys():
    print(key)

for key in my_family.keys():
    value=my_family[key]
    print(key,value)

for key, value in my_family.items():
    print(key,value)