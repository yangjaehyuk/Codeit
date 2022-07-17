class User:
    def __init__(self,name,email,password): # 특수 메소드: 특정 상황에서 자동으로 호출되는 메소드 __init__메소드는 인스턴스가 생성될 때 자동으로 호출
        self.name=name
        self.email=email
        self.password=password

user1=User("Young","young@codeit.kr","123456")
# 1. User 인스턴스 생성
# 2. __init__메소드 자동 호출

user2=User("Yoonsoo","yoonsoo@codeit.kr","abcdef")


user3=User("Taeho","taeho@codeit.kr","123abc")


user4=User("Lisa","lisa@codeit.kr","abc123")


print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)