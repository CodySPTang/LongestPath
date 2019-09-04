import sys


def findPath(arr, paths, xPos, yPos):
    left = 0
    right = 0
    up = 0
    down = 0
    if(paths[xPos][yPos] != -1):
        return paths[xPos][yPos]
    if(xPos > 0):
        if(arr[xPos - 1][yPos] > arr[xPos][yPos]):
            left = findPath(arr, paths, xPos - 1, yPos) + 1
    if(xPos < (len(arr) - 1)):
        if(arr[xPos + 1][yPos] > arr[xPos][yPos]):
            right = findPath(arr, paths, xPos + 1, yPos) + 1
    if(yPos > 0):
        if(arr[xPos][yPos - 1] > arr[xPos][yPos]):
            down = findPath(arr, paths, xPos, yPos - 1) + 1
    if(yPos < (len(arr[xPos]) - 1)):
        if(arr[xPos][yPos + 1] > arr[xPos][yPos]):
            up = findPath(arr, paths, xPos, yPos + 1) + 1
    paths[xPos][yPos] = max([left, right, up, down])
    return paths[xPos][yPos]


def getPathArr(arr):
    path = list(map(list, arr))

    x = 0
    while x < len(path):
        y = 0
        while y < len(path[x]):
            path[x][y] = -1
            y += 1
        x += 1
    return path

def traverseArr(arr):
    paths = getPathArr(arr)
    x = 0
    while x < len(arr):
        y = 0
        while y < len(arr[x]):
            paths[x][y] = findPath(arr, paths, x, y)
            y += 1
        x += 1
    longest = max(map(max, paths)) + 1
    return longest

def main():
    test = [[9, 9, 4], [7, 7, 8], [2, 1, 1]]
    print(traverseArr(test))

if __name__ == "__main__":
    main()
