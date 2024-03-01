#named tuples

# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email


# users = (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com')
# print(users[1])
#
# user = User(users[0],users[1],users[2],users[3],users[4])
# print(user.age)
#
# users = [
#     (1,'Toxir','Toxirov',28,'toxir@gmail.com'),
#     (2,'Sobir','Toxirov',28,'toxir@gmail.com'),
#     (3,'Jalil','Toxirov',28,'toxir@gmail.com'),
#     (4,'BAkir','Toxirov',28,'toxir@gmail.com'),
# ]
#
# for user in users:
#     employee = User(*user)
#     print(employee.email)

# ------------------------------------------------------------------
# from collections import namedtuple
#
# User = namedtuple('User','id name lastname age email')
#
# users = [
#     (1,'Toxir','Toxirov',28,'toxir@gmail.com'),
#     (2,'Sobir','Toxirov',28,'toxir@gmail.com'),
#     (3,'Jalil','Toxirov',28,'toxir@gmail.com'),
#     (4,'BAkir','Toxirov',28,'toxir@gmail.com'),
# ]
#
# for user in users:
#     us = User(*user)
#     # print(*us)
#     print(us.id,us.name,us.lastname,us.age,us.email)
#------------------------------------------------------------------------------------------
# from collections import namedtuple
#
# Car = namedtuple('Car','name color speed ruller price tipe')
#
# cars = [
#     ('Malibu', 'Red', '300k/h', 2000, 4, 'Avtomat'),
#     ('Ferrari', 'Black', '500k/h', 90000, 2, 'Avtomat'),
#     ('Pogani', 'Black', '900k/h', 11000, 2, 'Avtomat'),
# ]

# for car in cars:
#     us = Car(*car)
#     print(*us)
    # print(us.name,us.color,us.speed,us.ruller ,us.price, us.tipe)