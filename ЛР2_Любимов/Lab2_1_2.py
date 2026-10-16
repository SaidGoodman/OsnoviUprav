cities = tuple(input("Введите названия городов: ").split())
result = ()
for city in cities:
    if city != "Самара":
        result += (city,)

print("Города без Самары: ", " ".join(result))
