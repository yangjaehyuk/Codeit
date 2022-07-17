x=2 #글로벌변수
def my_function():
    x=3 #로컬변수
    print(x)

my_function()
print(x)

def square(x): #파라미터도 로컬변수
    return x*x

print(square(3))