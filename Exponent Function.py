
# 2 to the power of 3
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))

# in the function called raise_to_power we are taking 2 pieces of info base_num and pow_num.
# variable called result where we will store the result of the math
# for loop. i wanna loop through this range of numbers(pow_num)
# every time through the loop we are just multiplying the result by base_num then returning result