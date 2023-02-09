#crete a program for ticket price if below are the condition:
#if the height is => 120 cm they can ride ramjhoola
#if the age < 120cm they can not ride ramjhool
#if the age is <= 12 pay ₹ 5
#if the age is =< 18(from 12yr upto 18yr) pay ₹ 7
#if the age is > 18 pay ₹ 12
#if anyone want photo they have to pay extra ₹ 3 no matter what is there age:
print("Welcome to the Durga puja Ramjhoola")
height = int(input("enter your height in cm: "))
if height >= 120:
    bill = 0
    print("They can ride on Ramjhoola")
    age = int(input("enter your age: "))
    if age <= 12:
        bill = 5
        print("your age is ", age, " you have to pay ₹ 5")
    elif age <= 18:
        bill = 7
        print("your age is ", age, " you have to pay ₹ 7")
    else:
        bill = 12
        print("your age is ", age, " you have to pay ₹ 12")

    want_photo = input("Do you want photo: enter in capital letter Y or N ")
    if want_photo == "Y":
        bill += 3
    print("Now, your final bill is ₹",bill,)


else:
    print("SORRY,They can not ride on Ramjhoola due to shortage of height")