# This distributes people into different groups based on the first letter of their name


# Created by Ishan Kashyap
# Created on 4/4/2021


def nameSort(people):
    sortDict = {}
    for i in people:
        try:
            sortDict[i[0]].append(i)
        except KeyError:
            sortDict[i[0]] = [i]
        except IndexError:
            pass
    return  sortDict


