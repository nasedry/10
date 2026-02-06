from collections import deque

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

stack.pop()
stack.pop()

print("Стан стеку:", stack)


def is_empty(stack):
    return len(stack) == 0


def peek(stack):
    if is_empty(stack):
        return None
    return stack[-1]


print("Стек порожній:", is_empty(stack))
print("Верхній елемент:", peek(stack))


text = input("Введіть рядок: ")
stack_text = []

for ch in text:
    stack_text.append(ch)

reversed_text = ""
while stack_text:
    reversed_text += stack_text.pop()

print("Реверс рядка:", reversed_text)


queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print("Черга:", list(queue))

queue.popleft()
print("Черга:", list(queue))
queue.popleft()
print("Черга:", list(queue))
queue.popleft()
print("Черга:", list(queue))


shop_queue = deque()

while True:
    print("1 — додати клієнта")
    print("2 — обслугувати клієнта")
    print("3 — показати чергу")
    print("0 — вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Ім'я клієнта: ")
        shop_queue.append(name)
    elif choice == "2":
        if shop_queue:
            print("Обслуговано:", shop_queue.popleft())
        else:
            print("Черга порожня")
    elif choice == "3":
        print("Черга:", list(shop_queue))
    elif choice == "0":
        break
    else:
        print("Невірний вибір")


student = {
    "ім'я": "Анастасія",
    "дані": (19, "ІПЗ-21")
}

student["середній бал"] = 4.5
print(student)

student["дані"] = (20, "ІПЗ-22")
print(student)

del student["середній бал"]
print(student)

for key, value in student.items():
    print(key, value)


marks = [5, 4, 5, 3, 4, 5, 3]
marks_dict = {}

for m in marks:
    if m in marks_dict:
        marks_dict[m] += 1
    else:
        marks_dict[m] = 1

print(marks_dict)


products = {}

while True:
    print("1 — додати товар")
    print("2 — видалити товар")
    print("3 — показати всі товари")
    print("0 — вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Назва товару: ")
        price = float(input("Ціна: "))
        products[name] = price
    elif choice == "2":
        name = input("Назва товару: ")
        if name in products:
            del products[name]
        else:
            print("Товар не знайдено")
    elif choice == "3":
        print(products)
    elif choice == "0":
        break
    else:
        print("Невірний вибір")
