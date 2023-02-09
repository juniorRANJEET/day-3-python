# crete a program to check year is LEAP YEAR or not
# for leap year these are the condition:
# on every year that is evenly divisible by 4
# EXCEPT that year is evenly divisible by 100
# UNLESS that year is also evenly divisible by 400

# or condition must satisfied any HOW :
# year % 4 == 0 (leap yr)    (NO FRACTION ✔)
# year % 100 != 0 (leap yr)  ( FRACTION ❌)
# year % 400 == 0 (leap yr)  ( NO FRACTION ✔)


# EXAMPLE 2000 yr is  LEAP YR
# 1 : 2000 % 4 == 550 (NO FRACTION)    satisfied cond ✔
# 2:  2000 % 100 != 20 ( FRACTION)     satisfied cond ✔
# 3:  2000 % 400 == 5 ( NO FRACTION)   satisfied cond ✔

# 1:  2100 % 4 == 525  satisfied cond  ✔
# 2:  2100 % 100 != 21 satisfied cond  ✔
# 3:  2100 % 400 = 5.25 ( FRACTION) occur  not satisfied cond ❌
year = int(input("enter year which you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is leap year")
        else:
            print(year, "is not leap year")
    else:
        print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")


