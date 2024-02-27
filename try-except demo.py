""" simple try-except example - Justine Lee """

# ask user to enter a number

# create Boolean variable for the loop
keep_asking = True

# while loop to keep asking until valid input
while keep_asking == True:
    # catch any errors
    try:
        num = int(input("Enter your favourite integer: "))
        keep_asking = False
    except:
        print("Please enter an integer")

print(f"Great, {num} is my favourite integer too!")


