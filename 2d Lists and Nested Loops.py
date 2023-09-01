# 2d list / 2d array
number_grid = [
    # col 1  col2  col3
    [1,       2,     3], # row 0
    [4,       5,     6], # row 1
    [7,       8,     9], # row 2
    [0]

]
# can select a specif part of the grid
# first number is [row] [col]
print(number_grid[2][1])

# NESTED FOR LOOP
for row in number_grid:
    for col in row:
        print(col)