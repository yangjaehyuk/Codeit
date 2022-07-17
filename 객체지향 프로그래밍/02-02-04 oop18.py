class Citizen:
    """주민 클래스"""
    drinking_age=19 #음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name=name
        self.__age=age
        self.__resident_id=resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id==id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age>= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self.__age) + "살입니다!"

    def get_age(self): #__age의 값을 읽을 수 있다
        return self.__age

    def set_age(self, value): # __age값을 설정할 수 있다
        self.__age = value

young=Citizen("younghoon kang", 18, "12345678")

print(young.get_age())

young.set_age(25)
print(young.get_age())



