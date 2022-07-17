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

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name,self.email)
    @classmethod #데코레이터
    def number_of_users(cls): #클래스 메소드의 특별한 규칙: 첫 번째 파라미터의 이름은 cls로 쓰기
        print("총 유저 수는: {}입니다".format(cls.count))

    #def number_of_users(self):
    #    print("총 유저 수는: {}입니다.".format(User.count)) # 인스턴스 메소드에서도 클래스 변수를 가져올 수 있다

#user1=User("강영훈","younghoon@codeit.kr","123456")
#user2=User("이윤수","yoonsoo@codeit.kr","abcdef")
#user3=User("서혜린","lisa@codeit.kr","123abc")

#클래스 메소드 사용
#User.number_of_users(user1)
#user1.number_of_users()
User.number_of_users()