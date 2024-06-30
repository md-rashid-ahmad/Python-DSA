### Question1:
Write a program that checks if a number entered by the user is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



### Question2:
Write a program that asks the user for a temperature in Celsius and checks if it is below freezing (0 degrees), at freezing, or above freezing.

temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("It is below freezing.")
elif temperature == 0:
    print("It is at freezing point.")
else:
    print("It is above freezing.")


Question3:
Write a program that asks the user for their age and tells them if they are eligible to vote (18 years or older).

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


Question4:
Write a program that asks the user for a number and checks if it is positive, negative, or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



Question5:
Write a program that asks the user for a year and checks if it is a leap year.

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



Question6:
Write a program that asks the user for a number and checks if it is within the range of 1 to 10 (inclusive).

number = int(input("Enter a number: "))
if 1 <= number <= 10:
    print("The number is within the range of 1 to 10.")
else:
    print("The number is outside the range of 1 to 10.")



Question7:
Write a program that asks the user for two numbers and checks if both numbers are positive.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
else:
    print("At least one number is not positive.")



Question8:
Write a program that asks the user for their age and checks if they are a teenager (13-19 years old).

age = int(input("Enter your age: "))
if 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")
