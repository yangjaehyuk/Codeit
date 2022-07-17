from random import randint

def generate_numbers(n):
    picked_numbers = []

    while len(picked_numbers) < n:
        num = randint(1, 45)  # 무작위

        if num not in picked_numbers:
            picked_numbers.append(num)

    return picked_numbers
print(generate_numbers(6))