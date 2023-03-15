# # split text
# def split_tex(function):
#     def wrapper():
#         func = function()
#         return func.split()
#
#     return wrapper
#
#
# def lower_text(function):
#     def wrapper():
#         func = function()
#         return func.lower()
#
#     return wrapper
#
#
# @split_tex
# @lower_text
# def hello():
#     return "Hello world"
#
#
# print(hello())
#
#
# def capitalize(function):
#     def wrapper(arg1, arg2):
#         arg1 = arg1.capitalize()
#         arg2 = arg2.capitalize()
#         func = function(arg1, arg2)
#         return func
#
#     return wrapper
#
#
# @capitalize
# def say_hello(name1, name2):
#     return f"Hello {name1}, Hello {name2}"
#
#
# print(say_hello("ahmad", 'john'))
#
# # a = [1, 2, 3]
# # b = [7, 8, 9]
# # print([(i + j) for i, j in zip(a, b)])
# # print([(x, y) for x in a if x % 2 != 0 for y in b])
#
# multiplier = lambda a, b: a * b
# print(multiplier(2, 3))
#
#
# def wrapper(n):
#     return lambda a: a * n
#
#
# item = wrapper(5)
# print(item(3))
#
#
# def fib(n):
#     p, q = 0, 1
#     while p <= n:
#         yield p
#         p, q = q, p+q
#
# x = fib(10)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(dir())
# print(help(x))
#
# def split_names(function):
#     def wrapper(full_name):
#         func = function(full_name)
#         return func.split()
#     return wrapper
#
# @split_names
# def get_name_list(full_name):
#     return full_name.capitalize()
#
# print(get_name_list("john doe"))
#
# # threading ##############################3
# #ACID
print("hello world")