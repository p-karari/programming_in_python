#2d lists and nested loops

#2d lists
number_grid = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    [0, 25, 53]
]

print(number_grid[2][1])

#nested for loop
i = 0
j = 0
width = 3
for row in number_grid:
    print(number_grid[i])
    for col in range(width):
        if j < 3 and i < 4:
             print(number_grid[i][j])
             j = j + 1

    j = 0



    i += 1