
y={'karthika':40,'devika':2,'anjana':1,'saniya':3}
I=list(y.items())
I.sort()
print('ascending order is',I)
I=list(y.items())
I.sort(reverse=True)
print('descending order is',I)
dict=dict(I)
