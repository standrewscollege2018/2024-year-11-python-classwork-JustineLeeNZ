""" demo of using lists - Justine Lee """

# create list to store student names
names = ["Angus","Thomas","William","Ash","Caitlin"]

# create a list of ages
ages = [15,15,15,15,15,21]
"""
# ask user for a position in list to display name from
index = int(input("Give me index:"))

# print 2nd item in the list
print(f"Hello {names[index]}")
"""
print(len(names))

# display all the names in the list
for i in range(0,len(names)):
    print(names[i])

# add name to end of list
names.append("Lennox")

print("added item end of list")
# display all the names in the list
for i in range(0,len(names)):
    print(names[i])


# delete from list
del(names[0])

print("Deleted first item")
# display all the names in the list
for i in range(0,len(names)):
    print(names[i])




