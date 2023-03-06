# print('hello')
# print("1+2*3")
# print(1+2*3)
# print("hi.\nwelcome.")
# print("hi.\rwelcome.")
# print("hi.\rwelcome to python class.\rwelcome to pygame")
# print("The file is stored in C:\\new folder")

# x = 1
# x + 1
# print("x=", x)

# score = 0
# print("my score is:", score)

# score = score + 1
# print("my score is:", score)

# score += 1
# print("my score is:", score)

# score = score - 1
# print("my score is:", score)

# score -= 1
# print("my score is:", score)

# s1 = 12
# s2 = 13
# s3 = 14
# ave = (s1 + s2 + s3) /3
# print("average is:",ave)

# try:
#     n1 = int(input('> '))
#     # print(type(n1))
#     n2 = int(input('> '))
#     print(n1/n2)
# except Exception as ex:
#     print("an error occured")
#     print(ex)


# print(3/2)
# print(3//2)
# print(3 % 2)
# print(4 % 2)

# با کمک حلقه چهار عدد بگیر و اعداد زوجشون رو در لیستی اضافه کن
# مجموع اعداد زوج را پرینت کن

# Basic comparisons
a = 4
b = 5
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than than b")
if a <= b:
    print("a is less than or equal to b")
if a >= b:
    print("a is greater than or equal to b")
# NOTE: It is very easy to mix when to use == and =.
# Use == if you are asking if they are equal, use =
# if you are assigning a value.
if a == b:
    print("a is equal to b")
# Not equal
if a != b:
    print("a and b are not equal")
# And
if a < b and a < c:
    print("a is less than b and c")
# Non-exclusive or
if a < b or a < c:
    print("a is less than either a or b (or both)")
# Boolean data type. This is legal!
a = True
if a:
    print("a is true")
if not a:
    print("a is false")
a = True
b = False
if a and b:
    print("a and b are both true")
a = 3
b = 3
c = a == b
print(c)
