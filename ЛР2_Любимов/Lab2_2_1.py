def digits_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def steps_to_zero(n):
    steps = 0
    while n > 0:
        n -= digits_sum(n)
        steps += 1
    return steps

num = int(input("Введите число: "))
print("Количество действий до получения нуля: ", steps_to_zero(num))
