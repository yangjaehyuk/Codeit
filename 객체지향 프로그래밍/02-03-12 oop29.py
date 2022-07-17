# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language=favorite_language

    def program(self):
        print("{}으로 프로그래밍합니다.".format(self.favorite_language))

# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level=tennis_level

    def play_tennis(self):
        print("{}반에서 테니스를 칩니다".format(self.tennis_level))

captain = Engineer("자바스크립트")
yoonsoo = TennisPlayer("고급")

# 각 클래스가 잘 작동하는지 확인
captain.program()
yoonsoo.play_tennis()

class EngineerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(self, favorite_language)
        TennisPlayer.__init__(self, tennis_level)


# 다중 상속을 받는 클래스의 인스턴스 생성
younghoon = EngineerTennisPlayer("파이썬", "초급")

# 두 부모 클래스의 메소드들을 잘 물려받았는지 확인
younghoon.program()
younghoon.play_tennis()
