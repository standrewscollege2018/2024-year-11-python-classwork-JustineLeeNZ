""" displays how old user will be in 2050 - Justine Lee """

# ask user for name
name = input("Name?")

# ask the user for their age
age = input("How old are you?")
age = int(age)

# check if age is in valid range
if age >= 0 and age<=120:
    # display their name and also their age in 2050
    print(f"{name}, in 2050 you will be {age+26} years old")
else:
    print("Age needs to between 0 and 120")
