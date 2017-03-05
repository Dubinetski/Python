# Раскрыть список [1, 2, 11, 5, [45, [4566, [5]], [[4]], [6]]](сделать его "плоским"):

givenList = [1, 2, 11, 5, [45, [4566, [5]], [[4]], [6]]]
print(givenList)

def planeList(List, rezult = []):
    for i in List:
        if type(i) == list:
            planeList(i)
        else:
            rezult.append(i)
    return rezult

print(planeList(givenList))
