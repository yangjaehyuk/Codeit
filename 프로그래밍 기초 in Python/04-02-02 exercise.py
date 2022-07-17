import random

# 코드를 작성하세요.
answer = random.randint(1,20)
i = 4
j = 1
while i>0:
    su = int(input('기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: '.format(i)))
    if answer == su:
        print('축하합니다. {}번 만에 숫자를 맞히셨습니다.'.format(j))
        break
    else:
        if (answer < su):
            print('Down')
        else:
            print('Up')
    i-=1
    j+=1
if (answer!=su and i < 1):
    print('아쉽습니다. 정답은 {}입니다.'.format(answer))