scores = {'Ch':100,'En':80,'Ma':95,'Na':90}
print(scores)
print(scores.get('Ma'))
print(scores['Ma'])
print(scores.get('Pc','N/A'))
#print(scores['Pc']) 會有KeyError
print(scores.pop('En'))
print(scores)
print(scores.pop('Pc','N/A'))
