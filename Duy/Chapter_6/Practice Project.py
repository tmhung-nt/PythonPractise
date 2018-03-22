tableData = [['apples','oranges','cherries','banana'],
			['Alice','Bob','Carol','David'],
			['dogs','cats','moose','goose',]]
			

def printTable():
    Column1 = []
    Column2 = []
    Column3 = []



    for a in tableData[0]:
        b = a.rjust(8)
        Column1 = Column1 + [b]

    for c in tableData[1]:
        d = c.rjust(5)
        Column2 = Column2 + [d]

    for e in tableData[2]:
        f = e.rjust(5)
        Column3 = Column3 + [f]

    for i in range(4):
        yeah = (Column1[i] + ' ' + Column2[i] + ' ' + Column3[i])
        print(yeah)

printTable()