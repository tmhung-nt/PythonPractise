
tableData = [['apples','oranges','cherries','banana'],
			['Alice','Bob','Carol','David'],
			['dogs','cats','moose','goose',]]

zip(*tableData)
print(*(''.join(t) for t in zip(*tableData)), sep="\n")