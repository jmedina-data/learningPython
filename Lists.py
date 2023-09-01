
# can put strings numbers booleans into lists
friends2 = ["Amanda", "Alex", "Anji", "Sonali", "Sonya"]

# prints list
print(friends2)

# prints index (thing in square brackets[]
# counting starts at 0
print(friends2[2])

# counting backwards starts at 1
print(friends2[-2])

# selecting index. everything starting from index 1 and after
print(friends2[1:])

# selecting index starting at 1 to everything before 3
print(friends2[1:3])

# LIST FUNCTIONS

lucky_numbers = [42, 8, 15, 16, 23,42]
friends = ["Michael", "Dwight", "Dwight", "Jim", "Oscar", "Toby"]

lucky_numbers.reverse()
lucky_numbers.sort()
friends.sort()

# extend function
# take a list and append another list to the end of it
friends.extend(lucky_numbers)

# append always gonna add to the end of the list
friends.append("Creed")

# insert to specific index in list
friends.insert(1, "KEllY")

# removes a list item
friends.remove("Jim")

# clears list
#friends.clear()

print(friends)
print(friends.index("Oscar"))
print(friends.count("Dwight"))

print(lucky_numbers)


