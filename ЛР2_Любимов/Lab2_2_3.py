def mean_and_std(numbers):
    count = 0
    total = 0
    for x in numbers:
        total += x
        count += 1
    mean = total / count
    squares = 0
    for x in numbers:
        squares += (x - mean) ** 2
    std = (squares / count) ** 0.5
    return mean, std

nums = list(map(float, input("Введите числа: ").split()))
result = mean_and_std(nums)
print("Результат (мат. ожидание, СКО): ", result)
