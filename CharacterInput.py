#Adrian Sharpless
#Last modification date: 1/8/2019

#This program will ask for a user's name and age.
#It will then greet the user and tell them what year they will turn 100.

user_name = str(input("Hello! What is your name? "))
user_age  = int(input("What is your age? "))
current_year = int(input("What is the current year? "))

years_until_hundred = 100 - user_age
final_number = current_year + years_until_hundred

print('Hello, ', user_name, '!')
print("You will be 100 in the year: ", final_number)
