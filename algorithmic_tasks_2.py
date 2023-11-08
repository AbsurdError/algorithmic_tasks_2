# class Student:
#     def __init__(self, name, age, direction, course, average_score):
#         self.name = name
#         self.age = age
#         self.direction = direction
#         self.course = course
#         self.average_score = average_score
#
#     def get_name(self):
#         print(f'ФИО: {self.name}')
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         print(f'Возраст: {self.age} лет')
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_direction(self):
#         print(f'Обучается на направлении: {self.direction}')
#
#     def set_direction(self, direction):
#         self.direction = direction
#
#     def get_course(self):
#         print(f'Обучается на: {self.course} курсе')
#
#     def set_course(self, course):
#         self.course = course
#
#     def get_average_score(self):
#         print(f'Средний балл оценок: {round(sum(self.average_score) / len(self.average_score), 1)}')
#
#     def set_average_score(self, average_score):
#         self.average_score = average_score
#
# student = Student('Митрошин Игорь Максимович', 12, 'Информатика', 2, [3, 4 , 5])
# student.set_name('Пугачёв Владимир Александрович')
# student.set_age(16)
# student.set_average_score([5, 4, 5, 4])
# student.get_name()
# student.get_age()
# student.get_direction()
# student.get_course()
# student.get_average_score()

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def get_info(self):
#         print(f'Прямоугольник со сторонами а = {self.side_a} и b = {self.side_b}\nИмеет:\nПлощадь = {self.get_area()}\nПериметр = {self.get_perimeter()}')
#
#     def get_area(self):
#         return self.side_a * self.side_b
#
#     def get_perimeter(self):
#         return 2 * self.side_a + 2 * self.side_b
#
# rectangle = Rectangle(4, 9)
# rectangle.get_info()

# class Automobile:
#     def __init__(self, make, model, year, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def get_make(self):
#         return self.make
#
#     def set_make(self, make):
#         self.make = make
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_year(self):
#         return self.year
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_mileage(self):
#         return self.mileage
#
#     def set_mileage(self, mileage):
#         self.mileage = mileage
#
#     def Info(self):
#         print(f'Автомобиль марки: "{self.make}",\nмодель: "{self.model}",\nгод выпуска: {self.year},\nпробег автомобиля: {self.mileage} км')
#
# car = Automobile('Mersedes-Benz', 'G-class', 2004, 680938)
# car.set_make('LADA')
# car.set_model('Granta')
# car.set_year(2019)
# car.set_mileage(301300)
# car.Info()

# class BankAccount:
#     def __init__(self, full_name, year, gender, account_number, balance):
#         self.__balance = balance
#         self.full_name = full_name
#         self.year = year
#         self.gender = gender
#         self.account_number = account_number
#         self.__transactions = []
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f'Внесение наличных на счет: {amount}')
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f'Снятие наличных: {amount}')
#         else:
#             print('На счёте недостаточно средств')
#
#     def history(self):
#         print(f'ФИО: {self.full_name}\nВозраст: {self.year}\nПол: {self.gender}\nНомер счёта: {self.account_number}')
#         for transactions in self.__transactions:
#             print(transactions)
#
#         print(f'Итоговый баланс: {self.__balance}')
# # создаем объект счета с балансом 100000
# account = BankAccount('Иванов Иван Иванович',19,'Муж', 'NFH98756KI65', 100000)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # печатаем историю операций
# account.history()


# class Triangle:
#     def __init__(self, side_a, side_b, side_c):
#         self.side_a = side_a
#         self.side_b = side_b
#         self.side_c = side_c
#
#     def type_triangle(self):
#         if self.side_a == self.side_b == self.side_c:
#             return "равносторонним"
#         elif self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c:
#             return "равнобедренным"
#         else:
#             return "разносторонним"
#
#     def square_triangle(self):
#         pol = (self.side_a + self.side_b + self.side_c) / 2
#         square = round(((pol * (pol - self.side_a) * (pol - self.side_b) * (pol - self.side_c)) ** 0.5), 2)
#         return square
#
#     def info(self):
#         print(f'Треугольник со сторонами а = {self.side_a}, b = {self.side_b}, c = {self.side_c}\nТреугольник является "{self.type_triangle()}"\nПлощадь треугольника: {self.square_triangle()}')
#
# t = Triangle(3, 4, 5)
# t.info()