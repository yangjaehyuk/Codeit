#return문의 역할 1. 함수 즉시 종료하기 2. 값 돌려주기
def square(x):
    print("함수 시작")
    return  x*x
    print("함수 끝") # 바로앞에 있는 return문이 함수를 종료시키므로 출력되지 않는다

print(square(3))
print("Hello World!")