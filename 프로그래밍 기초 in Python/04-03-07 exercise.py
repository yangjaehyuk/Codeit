with open('vocabulary.txt', 'r', encoding='UTF=8') as f:
    for line in f:
        data=line.strip().split(":")
        kor=data[1]
        eng=data[0]
        a=input(kor+":")
        if a==data[0]:
            print('맞았습니다!')
        else:
            print('아쉽습니다. 정답은 {}입니다.'.format(eng))
