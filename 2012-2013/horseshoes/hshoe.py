def input():
    file = open("hshoe.in")
    gridSize = int(file.readline().strip())

    grid = []
    for i in range(gridSize):
        grid.append(file.readline().strip())

    return(grid)