#crete a program for ticket price if below are the condition:
#if the height is => 120 cm they can ride ramjhoola
#if the age < 120cm they can not ride ramjhool
#if the age is =< 18 pay ₹ 7
#if the age is > 18 pay ₹ 12
print("Welcome to the Durga puja Ramjhoola")
height = int(input("enter your height in cm: "))
if height >= 120:
    print("They can ride on Ramjhoola")
    age = int(input("enter your age: "))
    if age <= 18:
        print("your age is ",age," you have to pay ₹ 7")
    else:
        print("your age is ",age, " you have to pay ₹ 12")
else:
    print("SORRY,They can not ride on Ramjhoola due to shortage of height")