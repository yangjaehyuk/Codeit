#오늘은 2019년 10월 29일입니다.
year=2019
month=10
day=29

print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day)) #첫번째 {}안에는 year가 들어가고, 두번째 {}에는 month가 들어가고, 세번째 {}에는 day가 들어간다
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day))
print(date_string.format(year,month,day+1)) #다음날 출력