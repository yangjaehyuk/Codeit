def print_hello():
    print("안녕하세요!")

def add_print_to(original): # original=print_hello
    def wrapper():
        print("함수 시작")
        original() # print_hello함수를 호출하는 것과 동일함
        print("함수 끝")
    return wrapper

print_hello = add_print_to(print_hello)

print_hello()