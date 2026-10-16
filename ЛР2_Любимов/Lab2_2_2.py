def product(arr):
    result = 1
    for x in arr:
        result *= x
    return result

def average(arr):
    return sum(arr) / len(arr)

for i in range(1, 4):
    arr = list(map(int, input(f"Введите массив {i}: ").split()))
    print(f"Произведение: {product(arr)}, среднее: {average(arr):.2f}")
