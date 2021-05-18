import datetime
from datetime import date, timedelta

# ------------------ Calculating user's current age ---------------------------
date1 = datetime.date.today()
year1 = date1.year
year2 = int(input("Enter your birth year: "))
age = year1 - year2
print(age)

# ----------------- Printing 10 dates, each 2 weeks apart----------------------

count = 0
current = datetime.date.today()
print(current)
while count <= 8:
    count += 1
    answer = current + timedelta(days=7)
    current = answer
    print(count, answer)
else:
    print("All ten dates are printed")





