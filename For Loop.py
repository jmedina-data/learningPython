
# loop through
# changes value after each iteration of the loop

# for then specify variable
# for each letter in the string Giraffe Academy do something
for letter in "Giraffe Academy":
    print(letter)

# loop through the values in side of the array
friends = ["Jim", "Karen", "Kevin"]
# you can name the variable whatever you want.
# doesnt have to be friend
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

# can loop through range of numbers
for indexy in range(3, 10):
    print(indexy)

# print out all the elements in the array
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")
