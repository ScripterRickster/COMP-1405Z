# Made by Ricky L.

y = int(input("Enter the year: "))

print(f"\n{y} is a leap year" if y%4 == 0 and (y%100 != 0 or y%400 == 0) else f"\n{y} is not a leap year")
