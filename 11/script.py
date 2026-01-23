numbers_input = input("Введіть цілі числа через пробіл: ")
numbers_list = list(map(int, numbers_input.split()))
numbers_set = set(numbers_list)

print("Сформована множина:", numbers_set)

limit = int(input("Введіть число для порівняння: "))

count = 0
for num in numbers_set:
    if num > limit:
        count += 1

print("Кількість елементів, більших за", limit, ":", count)

def sum_of_set(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result_sum = sum_of_set(numbers_set)
print("Сума всіх елементів множини:", result_sum)

def check_number(numbers):
    check = int(input("Введіть число для перевірки: "))
    found = False
    for num in numbers:
        if num == check:
            found = True
            break

    if found:
        print("Число", check, "належить множині.")
    else:
        print("Число", check, "не належить множині.")

check_number(numbers_set)
