def printTable(dataLists):
    colWidths = [0] * len(dataLists)
    print(colWidths)
    for i in colWidths:
        colWidths = max(dataLists[i], key=len)
    y = len(colWidths)
    print(colWidths)

    for x in range(len(dataLists[0])):
        print(str(dataLists[0][x]).ljust(y) + str(dataLists[1][x]).center(y) + str(dataLists[2][x]).center(y))

tableData = [['apples','orangesajhahahah','cherries','bananas','carrots'],
             ['Alicesasdasda','Bobahhahahahahahahahah','Carol','David','Georgesssss'],
             ['dogs','catsasdadsasd','moose','goose','Marc']]

printTable(tableData)
