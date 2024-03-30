#Age Calculator:

age = int(input("What is your age in days?"))
page = (age // 1200) + (age % 1200 > 0)
remainder = (age % 1200)
row = (remainder // 30)
realrow = (row + 1)
column = (remainder % 30)
realrealrow = str(realrow)
realcolumn = str(column)
realpage = str(page)
print("Place your pin on page " + realpage + ", row " + realrealrow + ", column " + realcolumn + ".")
