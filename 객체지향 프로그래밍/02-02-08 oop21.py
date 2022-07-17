# _(언더바) 한개는 아무런 기능x, 경고메시지임(변수/메소드는 클래스 외부에서 직접 접근하지 마세요!)
# 파이썬에서 캡슐화를 할 때 변수/메소드 앞에 _(언더바) 한개만 붙인다
class Citizen:
    """주민 클래스"""
    drinking_age=19 #음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name=name
        self.set_age(age)
        self._resident_id=resident_id

    def authenticate(self, id_field): # getter/setter 메소드를 꼭 만들 필요는 없다
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id==id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age>= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self._age) + "살입니다!"

    def get_age(self): #__age의 값을 읽을 수 있다, getter 메소드
        return self._age

    def set_age(self, value): # __age값을 설정할 수 있다, setter 메소드
        if value<0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age=0
        else:
            self._age=value

young=Citizen("younghoon kang", 15, "12345678")

print(young.get_age)
print(young._resident_id)

young.set_age(20)
print(young._age)