from abc import ABC, abstractmethod
import time

class Order:
    def __init__(self, order_id, amount):
        self.id = order_id
        self.amount = amount

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_all(self):
        return self.orders

class OrderView:
    def menu(self):
        print("\n1. Додати замовлення\n2. Показати замовлення\n3. Загальна сума\n0. Вихід")
        return input("Вибір: ")

    def get_order_data(self):
        return int(input("ID: ")), float(input("Сума: "))

    def show_orders(self, orders):
        for o in orders:
            print(o.id, o.amount)

    def show_total(self, total):
        print("Загальна сума:", total)

    def message(self, text):
        print(text)

class IPriceStrategy(ABC):
    @abstractmethod
    def calculate(self, amount): pass

class NoDiscount(IPriceStrategy):
    def calculate(self, amount):
        return amount

class RegularDiscount(IPriceStrategy):
    def calculate(self, amount):
        return amount * 0.9

class BulkDiscount(IPriceStrategy):
    def calculate(self, amount):
        return amount * 0.8

class PriceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, amount):
        return self.strategy.calculate(amount)

class Observer(ABC):
    @abstractmethod
    def update(self, order): pass

class Logger(Observer):
    def update(self, order):
        print("Log: створено замовлення", order.id)

class Statistics(Observer):
    def __init__(self):
        self.count = 0

    def update(self, order):
        self.count += 1
        print("Статистика: замовлень =", self.count)

class OrderService:
    def __init__(self, repo):
        self.repo = repo
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, order):
        for o in self.observers:
            o.update(order)

    def create(self, order):
        self.repo.add(order)
        self.notify(order)

class ServiceDecorator:
    def __init__(self, service):
        self.service = service

    def create(self, order):
        self.service.create(order)

class LoggingDecorator(ServiceDecorator):
    def create(self, order):
        print("Декоратор логування")
        super().create(order)

class TimeDecorator(ServiceDecorator):
    def create(self, order):
        start = time.time()
        super().create(order)
        print("Час:", round(time.time() - start, 5))

class OrderController:
    def __init__(self, view, service, calculator, repo):
        self.view = view
        self.service = service
        self.calc = calculator
        self.repo = repo

    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                i, a = self.view.get_order_data()
                price = self.calc.calculate(a)
                self.service.create(Order(i, price))
            elif choice == "2":
                self.view.show_orders(self.repo.get_all())
            elif choice == "3":
                total = sum(o.amount for o in self.repo.get_all())
                self.view.show_total(total)
            elif choice == "0":
                break
            else:
                self.view.message("Помилка")

repo = OrderRepository()
view = OrderView()
calculator = PriceCalculator(NoDiscount())

service = OrderService(repo)
service.subscribe(Logger())
service.subscribe(Statistics())

service = TimeDecorator(LoggingDecorator(service))

controller = OrderController(view, service, calculator, repo)
controller.run()
