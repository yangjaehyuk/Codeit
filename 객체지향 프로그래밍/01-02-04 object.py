class User:
    def say_hello(some_user):
        #인사 메시지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))
    def login(some_user, my_email, my_password):
        #로그인 메소드
        if (some_user.email==my_email and some_user.password==my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")
    
user1=User()
user2=User()
user3=User()

user1.name="김대위"
user1.email="captain@codeit.kr"
user1.password="12345"

user2.name="강영훈"
user2.email="younghoon@codeit.kr"
user2.password="98765"

user3.name="최지웅"
user3.email="jiwoong@codeit.kr"
user3.password="78945"

User.say_hello(user1) # =user1.say_hello()
user1.say_hello() # 인스턴스 메소드 사용하기, 자동으로 user1이 say_hello의 파라미터안에 들어감

user1.login("captain@codeit.kr", "12345") #user1 인스턴스가 자동으로 첫번째 파라미터로 감 그래서 첫번째 파라미터를 빼고 나머지 파라미터만 적어야한다

