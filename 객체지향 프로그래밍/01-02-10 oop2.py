class User:
    def __init__(self,name,email,password):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name=name
        self.email=email
        self.password=password
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        # print함수를 호출할 때 자동으로 사용됨 return값이 출력됨
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

user1=User("강영훈","younghoon@codeit.kr","123456")
user2=User("이윤수","yoonsoo@codeit.kr","1q2w3e4r")

print(user1)
print(user2)