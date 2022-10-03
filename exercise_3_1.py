# https://www.py4e.com/html3/03-conditional
# Exercise 3.1  Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fh = float(hours)
except:
    fh = 0
try:
    fr = float(rate)
except:
    fr = 0

if fh > 40:
    # Overtime
    ovtH = fh - 40
    ovtP = ovtH * (fr * 1.5)
    pay = (40 * fr) + ovtP
else:
    # Regular
    pay = fh * fr

print("Pay:", pay)