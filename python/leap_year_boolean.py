def is_leap(year):
    leap = False
    if (year%4==0):
        print("True")
    elif (year%400==0):
        print("True")
    else:
        return leap
    return leap
year = int(input())
print(is_leap(year))
