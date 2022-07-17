def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.
    count=0
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if(list_1[i]==list_2[j]):
                count+=1
    return count


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    count=0
    special=0
    for i in range(len(numbers)):
        for j in range(len(winning_numbers)):
            if(numbers[i]==winning_numbers[j]):
                count+=1
                if(numbers[i] == winning_numbers[len(winning_numbers) - 1]):
                    special += 1
                    count -= 1
    if count == 6:
        return 1000000000
    elif count == 5 and special == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))