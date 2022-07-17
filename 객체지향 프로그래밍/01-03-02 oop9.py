class User:
    count=0
    def __init__(self,name,email,password):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name=name
        self.email=email
        self.password=password

        User.count+=1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

user1=User("Young","young@codeit.kr","123456")

print(type(user1))

print(type(2)) #정수
print(type("string")) #문자열
print(type([])) #리스트
print(type({})) #딕셔너리
print(type(())) #튜플

def print_hello():
    print("안녕하세요!")

print(type(print_hello)) #함수

int_list=[]

int_list.append(1)
int_list.append(3)
int_list.append(7)

print(int_list)