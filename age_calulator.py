#Age Calculator:
from datetime import datetime

def calculate_age_in_days(dob):
    # Parse the date of birth string into a datetime object
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the age in days
    age_in_days = (current_date - dob_date).days
    
    return age_in_days

#Calculator  
dob = input("What is your date of birth? Format: YYYY-MM-DD: ")
age = calculate_age_in_days(dob)
page = (age // 1200) + (age % 1200 > 0)
remainder = (age % 1200)
row = (remainder // 30)
realrow = (row + 1)
column = (remainder % 30)
if column == 0:
    column = 30
    realrow = (realrow - 1)  

print("Place your pin on page " + str(page) + ", row " + str(realrow) + ", column " + str(column) + ".")
print("You are " + str(age) + " days old.")

