age=int(input("Please enter your age:"))
DOB=int(input("Please enter your year of birth:"))
current_year=int(input("Please enter the current year:"))
if DOB==current_year:
    print("You are a new born baby.")
elif DOB>current_year:
    print("You are not born yet.")
elif DOB<current_year:
    print(f"You will be 100 year in {DOB+100}")
else:
    print("Please enter a valid input.")
ins_year=int(input("Enter the year in which yo want to know your age:"))
print(f"You will be {ins_year-DOB} years old in {ins_year}.")