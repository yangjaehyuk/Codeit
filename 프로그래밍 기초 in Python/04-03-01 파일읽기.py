
with open('data/Chicken.txt', 'r', encoding='UTF-8') as f: #'r'=read 파일을 쓸 때:'w' write
    for line in f:
        print(line.strip())