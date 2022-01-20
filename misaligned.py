
def printColorMap():
    majorColors = ["White", "Red", "Black", "Yellow", "Violet"]
    minorColors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(majorColors):
        for j, minor in enumerate(minorColors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(majorColors) * len(minorColors)


result = printColorMap()
assert(result == 25)
print("All is well (maybe!)\n")
