class BankAccount:
    """은행 계좌 클래스"""
    interest=0.02
    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name= owner_name
        self.balance=balance
    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance+=amount

    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balance<amount:
            print("Insufficient balance!")
        else:
            self.balance-=amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance*=1+BankAccount.interest

help(BankAccount) #클래스 내의 dockstring코드를 보여줌

help(list)