# key value pairs
# word is the key
# definition is the value
# all the keys have to be unique. no dupes.

monthConversions = {
#    Key     Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    69: "LOL"
# can also assign numbers as keys as long as its unique
}

# its giving the value of the key
print(monthConversions[69])

print(monthConversions.get("Dec", "Not a valid Key"))