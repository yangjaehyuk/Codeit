def add_print_to(original): # original=print_hello
    def wrapper():
        print("함수 시작")
        original() # print_hello함수를 호출하는 것과 동일함
        print("함수 끝")
    return wrapper

@add_print_to # print_hello함수를 add_print_to로 꾸며주라는 의미
def print_hello():
    print("안녕하세요!")

print_hello()