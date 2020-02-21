# to check whether a given year is leap or # NOTE:
year=int(input("Enter your year : "))

if((year%4 is 0 and year%100 is not 0) or (year%4 is 0 and year%100 is 0 and year%400 is 0)):
    print("Leap year.")
else:
    print("Not a leap year.")
