multList = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

# print the middle column

print([col[1] for col in multList])


# Get the diagonal, [i][i] will get the [0][0], then [1][1], then [2][2]
print([multList[i][i] for i in range(len(multList))])