# print("Hello World")

# name = input("What is your name?")
# print(name)

# name = "Jack"
# print(name)

# name = "Angela"
# print(name)

# print(len(input("What is your name?")))

# name = input("What is your name?")
# length = len(name)
# print(length)

# print("Welcome to the band name generator")
# city = input("Which city did you grew up in?")
# pet = input("What is the name of your pet?")
# print(city + " " + pet);

# #Strings
# print("Hello"[0])
#
# print("123" + "345")
#
# #Integer
# print(123+345)
#
# #Float
# print(3.141 + 98.181)
#
# #Boolean
#
# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# # print(type(num_char))
# print("Your name has " + new_num_char + " characters.")

# a = 123
# print(type(a))
#
# print(70 + float("100.5"))

# print(str(70) + str(70))

# two_digit_number = input("Type a two digit number")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
#
# print(first_digit)
# print(second_digit)
#
# result = int(first_digit) + int(second_digit)
#
# print(result)

# height = input("Enter your height in m:")
# weight = input("Enter your weight in kg:")
#
# bmi = int(weight)/(float(height) ** 2)
#
# print(round(bmi))
# print(float(bmi))
# print(int(bmi))

# score = 0
# height = 1.8
# isWinning = True
#
# #f-string
#
# print(f"your score is {score}, {height}, {isWinning}")

# age = input("What is your current age?")
# age_as_int = int(age)
#
# age_left = int(90 - age_as_int)
#
# months_left = age_left * 12
# weeks_left = age_left * 52
# days_left = age_left * 365
#
# print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months")


# total_bill = float(input("What was the total bill? $"))
# tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15"))
# number_of_people = int(input("How many people to split the bill?"))
#
# tip_amount = float((total_bill * tip_percentage)/100)
#
# print(f"Your tip is {tip_amount}, therefore your total is $ {total_bill + tip_amount}")

# CONDITIONAL

# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("You can ride the roller coaster")
# else:
#     print("You cannot ride the roller coaster")

# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("The number is even")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("The number is odd")

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
# bmi = round(weight/(float(height) ** 2))

# BMI CALCULATOR
# if bmi < 18.5:
#     print(f"You are underweight because your BMI is {bmi}")
# elif bmi < 25:
#     print(f"You are normal weight because your BMI is {bmi}")
# elif bmi < 30:
#     print(f"You are overweight because your BMI is {bmi}")
# elif bmi < 35:
#     print(f"You are obese because your BMI is {bmi}")
# else:
#     print(f"You are clinically obese because your BMI is {bmi}")

# year = int(input("Which year do you want to check?"))

# LEAP YEAR
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("not a leap year")

# ROLLER COASTER WITH AGE AND PHOTOS
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the roller coaster")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#
#     if wants_photo == "Y":
#         bill = bill + 3
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# PIZZA DELIVERY

# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want? S,M,L,XL ")
# add_chicken = input("Would you like to add chicken? Y/N ")
# extra_cheese = input("Would you like to add cheese? Y/N ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_chicken == "Y":
#     if size == "S":
#         bill = bill + 2
#     else:
#         bill = bill + 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is {bill}")

# LOVE CALCULATOR
# print("Welcome to the love calculator")
# name1 = input("What is your name?")
# name2 = input("What is their name?")
#
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
#
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
#
#
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together like coke and mentos")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together")
# else:
#     print(f"Your score is {love_score}")

# TREASURE ISLAND
# print("Welcome to the Treasure Island, Your mission is to find the treasure")
# choice1 = input('You\'re at a crossroad, where do you want to ? Type "left" or "right" ').lower()
#
# if choice1 == "left":
#     choice2 == input("type wait or swim").lower()
#     if choice2 == "wait":
#         choice3 == input("Pick one color. Red or Blue or Yellow").lower()
#         if choice3 == "red":
#             print("game over")
#         elif choice3 == "blue":
#             print("game over")
#         elif choice3 == "yellow":
#             print("You've found the treasure")
#     else:
#         print("You got attacked by angry bird")
# else:
#     print("You fell into a hole. Game over.")
# import random
# import my_module
#
# print(f"This is import from my_module {my_module.pi}")
#
# random_integer = random.randint(1, 10)
# print(f"This is random integer {random_integer}")
#
# random_float = random.random() * 5
# print(f"This is random float {random_float}")

# import random
#
# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Head")
# else:
#     print("Tails")

# states_of_america = ["Delaware", "California", "Texas", "North Dakota"]
#
# states_of_america[1] = "C"
# states_of_america.append("Florida")
# states_of_america.extend([1,2,3,4,5])
#
# print(states_of_america)
# import random
# names_string = input("Give me everybody's names, separated by a comma ")
# names = names_string.split(",")
# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay)
# random.randint(0,)

# TREASURE MAP
# row1 = ["", "", ""]
# row2 = ["", "", ""]
# row3 = ["", "", ""]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = (map[vertical - 1])
# selected_row[horizontal - 1]

# ROCK, PAPER & SCISSORS
# import random
#
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Paper "))
# computer_choice = random.randint(0,2)
#
# print(f"You choose {user_choice}")
# print(f"Computer choose {computer_choice}")
#
# if user_choice == 0 and computer_choice == 2:
#     print("You won")
# elif computer_choice > user_choice:
#     print("You lose")
# else:
#     print("Invalid number")

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# student_heights = [20,30,40,50,60,70,80,90]
#
# for height in student_heights:
#     print((sum(student_heights)/(len(student_heights))))

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
#
# number_of_students = 0;
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(max(student_scores))
# print(min(student_scores))
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# sum_even = 0
# for number in range(2, 100, 2):
#     sum_even += number
#     # print(number)
#     print(f"This will calculate sum in every step {sum_even}")
# print(f"This will calculate the total sum {sum_even}")

# FIZZ-BUZZ
# for number in range(1, 100):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"FizzBuzz {number}")
#     elif number % 5 == 0:
#         print(f"Buzz {number}")
#     elif number % 3 == 0:
#         print(f"Fizz {number}")
#     else:
#         print(number)

# PASSWORD GENERATOR
# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
#
# print("Welcome to the PyPassword Generator!")
#
# nr_letters = int(input("How many letters would you like to in your password?\n "))
# nr_numbers = int(input("How many numbers would you like to in your password?\n "))
# nr_symbols = int(input("How many symbols would you like to in your password?\n "))
#
# password_list = []
#
# for char in range(1, nr_letters + 1):
#     # random_char = random.choice(letters)
#     # password += random_char
#     password_list += random.choice(letters)
#
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#     # print(password)
# print(password)

























