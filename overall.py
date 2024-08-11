#Day - 1 (Variables)
# print (len("Hello World!\nHello World!"))
# num1 = int(input())
# num2 = int(input())
#
# print(num1 * num2)
#
# name = input("what is your name")

# a = input("Type your name")
# b = input("Type your surname")
# c = a
# d = b
# a = d
# b = c
# print(a)
# print(b)

city_name = input("What's the name of the city you were born in?\n")
pet_name = input("What was your pet's name?\n")
print("Your band name could be " + city_name + " " + pet_name)


#Day - 2 (Data Types, Manipulate Strings, f-Strings)
# print("Hello"[4])
#
# print(len("ckjbwjkwcwjcnw"))
#
# print(type("zdravko"))
# print(type(True))
# print(type(234))
# print(type(200.78))


#print("Print the numbers of letters in your name " + len(input("What is your name\n"))

# name_of_the_user = input("What is your name\n")
# number_of_letters = len(name_of_the_user)
#
# print("Print the number of letters in your name: " + str(number_of_letters))

# print(2**2)
# print(2/2)
# print(2//2)
# print(2*2)
# print(2+2)
# a = 5
# b = 7
# print(a+b)
# print(2-2)
#
# print(3*3+3/3-3)
# print(3*(3+3)/3-3)

# bmi = 90/1.75**2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2))

#f-Strings
# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is {score}, your height is {height} ")
#
# ######################################################################################
#
# print("Welcome to the tip calculator")
#What was the total bill? $150
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 5
#Each person should pay: 33.67


print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_total = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
split = ((total_bill * (tip_total/100+1)/people))
split = round(split, 2)
print(f"Each person should pay: ${split}")


#Day - 3 (Control Flow, Logical Operators)
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?\n"))
# if height >= 120:
#     print("Enjoy your ride")
# else:
#     print("You are too small. Sorry.")


