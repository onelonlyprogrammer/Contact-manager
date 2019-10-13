FILENAME = "null.txt"
def writeToFile(towrite):
    with open(FILENAME, "w") as file:
        for i in towrite:
            for x, y in i.items():
                file.write(x + ", " + y + "\n")

def readFromFile():
    ret = {}
    with open(FILENAME, "r") as file:
        for f in file:
            ret[f.split(", ")[0]] = f.split(", ")[1].strip("\n")

    return ret
