""" demo of while loops - Justine Lee """

# not a useful way to use while loop
# for loop does this better

i = 0

while i < 10:
    print(i)
    i = i + 1

print("All done")



# ask user for name and print hello message

keep_asking = True

while keep_asking == True:
    name = input("Enter your name: ")


    if name == "stop":
        keep_asking = False
    else:
        print(f"Hello {name}")






