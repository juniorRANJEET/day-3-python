# create a program tp workout love score between toe people ie. love calculator program
# take both people name and check for the number of times the latter in the words of TRUE occur ,then again check for the number of times the letter in the words of LOVE occur. Then combine these words to make two digit number
# where for love score less than 10 or 90 message would be "your score is X you together like coke and mentos."
# where for love score between 40 and 50 message would be "your score is Y you are alright together"
# otherwise your message would be "your score is Z"


print("welcome to love calculator")
name1 = input("what is your name: \n")
name2 = input("what is their name: \n")
combine_name = name1 + name2
lower_case_string = combine_name.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90) :
    print(f"your love score is {love_score},you go together like coke and mentos")
elif (love_score >= 40) and (love_score <=50):
    print(f"you love score is {love_score}, may go together")
else:
    print(f"your score is {love_score}")