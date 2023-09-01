

# boolean values


is_male = True

if is_male:
    print("you are male lol")
else:
    print("youre not male lol")


# OR
is_trans = True
is_tall = False
# or means when one or the other is true
# if they are trans or tall it executes if statement
if is_trans or is_tall:
    print("you are trans or tall or both")
# if not trans or tall it executes else satement
else:
    print("you neither male nor tall")


# AND
is_queer = True
is_tall = True
# and means both conditions have to be true
if is_trans and is_tall:
    print("you are a tall queer")
else:
    print("you are either not queer or not tall or both")


# else is = elif
is_bi = True
is_tall = True
# and means both conditions have to be true
if is_trans and is_tall:
    print("you are a tall bi")
elif is_bi and not(is_tall):
    print("you are a short bi")
elif not(is_bi) and is_tall:
    print("you are not bi but you are tall")
else:
    print("you are not not bi and not tall or both")