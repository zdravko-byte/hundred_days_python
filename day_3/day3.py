# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?\n"))
# if height >= 120:
#     print("Enjoy your ride")
#     age = int(input("What is your age "))
#     if age <= 12:
#         print("That would be $5")
#     elif age <= 18:
#         print("That would be $7")
#     else:
#         print("That would be $12")
# else:
#     print("You are too small. Sorry.")

# a = 10 % 3
# print(a)

# number = int(input("Please enter a number\n"))
# if number % 2 == 0:
#     print("The number you entered is an even number")
# else:
#     print("The number you entered is an odd number")


# Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())

# bmi = weight / (height ** 2)
# #bmi = round(bmi, 5)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")


print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
bill = 0
if height >= 120:
    print("Enjoy your ride")
    age = int(input("What is your age "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want a picture taken? Answer Y or N.\n")
    if photo == "Y":
        bill += 3
    print(f"Your total bill will be ${bill}")

else:
    print("You are too small. Sorry.")