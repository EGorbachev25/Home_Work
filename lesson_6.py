# Кортеж (tuple) – константний (immutable) список
# можна працювати як зі звичайним списком,
# тільки не можна нічого міняти (функції, які змінюють колекцію - відсутні в кортежі)
# crud -> create, read, update, delete (у кортежі можна робити лише read)

# info = ("test1", 123)
# print(info)
# print(type(info))
#
# info = "test2", 1234, 123445
# print(info)
# print(type(info))
# #
# print(info[0])

# info[0] = 123  # TypeError: 'tuple' object does not support item assignment

# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

#####
# import copy
#
# info = "test2", 1234, 123445
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)
# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

###########
# for num in 1, 3, 4, 5, 6, "Hello", 7:
#     print(num)
#
# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)
#
# for _ in range(5):
#     print("Hello")

# таку змінну створювати не можна так як оскільки її складно читати та зрозуміти
# _ = "Vasya"
# print(_)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

#############
##
# dict -> словник, колекція key: value

# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     2: "qwerty",  # дублювати ключі не можна!
# }
#
# print(users)
# print(type(users))
# print(users[1])  # [1] -> це не індекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])
#
# users_list = [
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# ]
#
# users_dict = dict(users_list)
# print(users_dict)
#
# users_list = list(users_dict)
# print(users_list)

###########
##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# print(users["+33333333"])
# users["+33333333"] = "Petya"
# print(users["+33333333"])
#
# users["+4444444"] = "Test"
# print(users["+4444444"])
#
# print(users)
#
# for key in users:
#     print(users[key], end=" ")
#
# print()
# #
# for key in users.keys():
#     print(key, end=" ")
#
# print()
# print(users.keys())
# print(list(users.keys()))
# #
# for value in users.values():
#     print(value, end=" ")
#
# print()
# print(users.values())
#
# print()
# for key, value in users.items():
#     print(f"key: {key} value: {value}")
#
# print()
# print(users.items())

#####
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# # print(users["+33333333"])
# print(users.get("+33333333", "key not exists"))
#
# # del users["+55555555"]
# deleted_value = users.pop("+555555551", "key not exists")
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

##
# users_1 = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# #
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)
#
# users_2 = {
#     "+11111111": "eeeeeee",
#     "+44444": "qqqqqq",
#     "+12341234": "wwwwwww"
# }
# #
# users_1.update(users_2)
# print(users_1)
# print(users_2)

################
# json
# users = {
#     "Vasya": {
#         "phone": "123123",
#         "email": "qwerty1@gmail.com",
#         "hobbies": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "1345555",
#         "email": "aqwfafdbsdb@gmail.com",
#         "hobby": "uerhukjshbdjbkhdf",
#         "add_data": {
#             1: "test-1",
#             2: "test-2",
#         }
#     }
# }

# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])
#
# print(users.get("Vasya").get("hobbies")[1])
# print(users.get("Petya").get("add_data").get(2))
##
# v1
# key = input("Enter key: ")
# if key in users:
#     print(users[key])
# else:
#     print("Nothing found!")

# v2
# key = input("Enter key: ").strip().lower()
# for curr_key in users.keys():
#     if curr_key.lower() == key:
#         print(users[curr_key])
#         break
# else:
#     print("Nothing found!")

##############
# # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# Дублікати значень буде видалено.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
#     users.remove(user)  # якщо немає значення – генерується виняток
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
# print(users)
# # #
# users.clear()
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# # copy() копіювання працює так само як і в list, dict і тд
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# # v2
# print(users & users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
# print(users3)  # {"Tom", "Alice"}
# # v2
# print(users - users2)
# #
# users.difference_update(users2)
# print(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
# print(users3)
#
# # v2
# users4 = users ^ users2
#
# ##
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers))  # True
# print(superusers.issubset(users))  # False
#
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers))  # False
# print(superusers.issuperset(users))  # True

#
# # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)
# users = set(users)
# print(users)
# # можна використовувати всі функції звичайного set, крім тих, що модифікують значення

#####################
import random

words = ['Apple', 'Banana', 'Cherry', 'Letter', 'Cat', 'Dog']

secret_word = words[random.randint(0, len(words) - 1)]

# print(secret_word)
# print("_" * len(secret_word))

user_word = ["_"] * len(secret_word)
# print(user_word)
# print(" ".join(user_word))

attempt_count = 0

while True:
    # v1
    if "".join(user_word).find("_") == -1:
        print(f"\nYou guessed a word {secret_word}!\nAttempts: {attempt_count}")
        break
    # # v2
    # if "".join(user_word).lower() == secret_word.lower():
    #     print(f"\nYou guessed a word {secret_word}!\nAttempts: {attempt_count}")
    #     break

    print(" ".join(user_word))

    letter = input("Enter letter: ").strip().lower()

    if not letter.isalpha() or len(letter) != 1:
        print("Please enter only one letter!")
        continue

    attempt_count += 1

    for i in range(len(secret_word)):
        if letter == secret_word[i].lower():
            user_word[i] = letter


# добавить ограничение на кол-во попыток, если не уложились в кол-во - проиграли

# добавить:
# - два уровня сложности
# легкий уровень: кол-во попыток равно длина слова * 2 -> если не угадал - вывести сообщение об этом
# сложный уровень: кол-во попыток равно длина слова * 1.5 -> если не угадал - вывести сообщение об этом
# показывать сколько попыток осталось
