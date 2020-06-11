import math
#The program requests the user to enter which calculation they want to calculate
#if the user enter word not required the program will tell the user
#if user writes investment the program will then ask all the investment question same goes if user writes bond

while True:
    data = input("Enter the type of calculation: ")
    if data.lower() not in ('bond', 'investment'):
        print("Enter only investment or bond")
    else:
        break

if data == "investment":
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    interest = input("Do you prefer simple or compound: ")

    if interest == "compound":
        compound_amount = principle * (pow((1 + rate / 100),time))

        print("compound amount is: {}".format(compound_amount))
    elif interest == "simple":
        simple_amount = principle * (1 + rate / 100) * time

        print("simple amount is: {}".format(simple_amount))

if data == "bond":
    house = float(input("what is the present value of the house: "))
    rating = int(input("Enter the interest value: "))
    months = int(input("Enter the number of months you plan to repay bond: "))

    payment = house * ((1 + rating ** months)) / ((1 + rating ** months) -1)

    print("The amount you will repay each month is: {}".format(payment))
