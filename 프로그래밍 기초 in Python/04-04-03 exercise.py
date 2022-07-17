from random import randint

def generate_numbers(n):
    picked_numbers = []

    while len(picked_numbers) < n:
        num = randint(1, 45)  # 무작위

        if num not in picked_numbers:
            picked_numbers.append(num)

    return picked_numbers


def draw_winning_numbers():
    # 코드를 작성하세요.
    a=generate_numbers(1)
    new_list = sorted(generate_numbers(6))
    new_list.append(a)
    return new_list

print(draw_winning_numbers())

