# print out name of favourite book or movie
print("My favourite movie is Star Wars")


# ask user for name
name = input("Name?")

# ask the user for their favourite book movie etc
movie = input("What is your favourite movie?")

# display a friendly message
#print("That's cool", name, ". I like the", movie, "movie too")
# same message but using a f-string - MUCH NICER TO USE!!!
print(f"That's cool {name}. I like the {movie} movie too")

# ask the user for their age
age = input("How old are you?")
age = int(age)
print(age)

# display message telling their age in 2050
#print("In 2050 you will be", age+26, "years old")

# use f-string to add their name and also to display the age+26
print(f"{name}, in 2050 you will be {age+26} years old")
