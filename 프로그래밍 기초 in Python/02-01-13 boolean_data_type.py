# 불린(boolean)
print(True)
print(False)

#and는 두 개가 True여야 True
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or는 두 개 중에 하나만 True면 True
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not은 True를 False로 만들어주고, False를 True로 만들어준다
print(not True)
print(not False)

#명제(숫자비교)
print(2>1)
print(2<1)
print(3>=2)
print(3<=3)
print(2==2) #2는 2와 같다
print(2!=2) #2는 2와 같지 않다

print("Hello"=="Hello")
print("Hello"!="Hello")

print(2>1 and "Hello"=="Hello") #True and True

print(not not True) #not False
print(not not False) #not True

print(7==7 or (4<3 and 12>10)) #True or False

x=3
print(x>4 or not(x<2 or x==3)) #False or False