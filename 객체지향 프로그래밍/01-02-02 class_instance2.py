class User:
    pass

user1=User()
user2=User()
user3=User()

user1.name="김대위" # 인스턴스 변수 정의하기: 인스턴스 이름. 속성이름(인스턴스 변수)="속성에 넣을 값"
user1.email="captain@codeit.kr"
user1.password="12345"

user2.name="강영훈"
user2.email="younghoon@codeit.kr"
user2.password="98765"

user3.name="최지웅"
user3.email="jiwoong@codeit.kr"
user3.password="78945"

#인스턴스 변수 사용하기: 인스턴스 이름. 인스턴스 변수 이름
print(user1.email)
print(user2.password)

print(user1.age) #인스턴스 변수를 사용하려면 그전에 미리 정의해 두어야함