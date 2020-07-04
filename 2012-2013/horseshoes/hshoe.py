def input():
    file = open("hshoe.in")
    gridSize = int(file.readline().strip())

    hsGrid = []
    for i in range(gridSize):
        hsGrid.append(file.readline().strip())

    return(hsGrid)

def main(hsGrid):
    if hsGrid[0][0] == ')':
        return('1')
    
    prevHs = ''
    flip = False
    for hsr in hsGrid:
        for hs in hsr:
            currentHs = hs
            if prevHs != '':
                if currentHs != prevHs:
                    flip = True    
            prevHs = currentHs