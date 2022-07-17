import calculator as calc#모듈
from calculator import add, multiply #calculator라는 모델에서 add함수와 multiply함수만 불러오겠다
#from calculator import * 인 경우 calculator안의 모든 함수를 불러오라는 뜻

print(calc.add(2,5))
print(calc.multiply(3,4))
print(add(2,5)) #from으로 불러올 경우 calc를 안써도 된다
print(multiply(3,4))