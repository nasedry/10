a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

print("\nАрифметичні операції:")
print("Додавання:", a + b)
print("Віднімання:", a - b)
print("Множення:", a * b)

if b != 0:
    print("Ділення:", a / b)
else:
    print("Ділення неможливе (ділення на нуль)")

print("\nПорівняння чисел:")
if a > b:
    print("Перше число більше за друге")
elif a < b:
    print("Перше число менше за друге")
else:
    print("Числа рівні")

text = input("\nВведіть рядок: ")
length = len(text)

print("Довжина рядка:", length)

if length < 5:
    print("Рядок короткий")
elif 5 <= length <= 10:
    print("Рядок середній")
else:
    print("Рядок довгий")

number = int(input("\nВведіть число для перевірки діапазону: "))

if number >= 10 and number <= 20:
    print("Число знаходиться в діапазоні від 10 до 20")
else:
    print("Число НЕ знаходиться в діапазоні від 10 до 20")
