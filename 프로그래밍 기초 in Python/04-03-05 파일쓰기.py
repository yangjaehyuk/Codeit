with open('new file.txt', 'a') as f: #w는 쓰기, a는 덮어쓰기 파일이 없어도 w대신 a를 사용할 수 있다
    f.write("Hello world!\n")
    f.write("My name is Codeit.")