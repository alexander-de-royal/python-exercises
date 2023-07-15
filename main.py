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


total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15"))
number_of_people = int(input("How many people to split the bill?"))

tip_amount = float((total_bill * tip_percentage)/100)

print(f"Your tip is {tip_amount}, therefore your total is $ {total_bill + tip_amount}")






