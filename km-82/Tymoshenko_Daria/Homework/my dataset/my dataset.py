"""
 Створити dataset та працювати з ним
"""

def create_dict(lst):
    if len(lst[0]) == 2:
        return {
            'Estimate': lst[0][0],
            'finalEstimate': lst[0][1]
                }
    dct={}

    for elem in lst:
        key = elem[0]
        if key not in dct:
            dct[key] = []
        dct[key].append(elem[1:])
    for key in dct:
        dct[key] = create_dict(dct[key])
    return dct
with open('adjusted-name-combinations-list.csv', encoding='utf-8') as f:
    f.readline()
    file = [[el.strip() for el in line.split(',')[1:]] for line in f]
    result = create_dict(file)
print(result)

import plotly.offline as pl
import plotly.graph_objs as go
# Top 10
quantity_name = dict()
for name in result:
    quantity_name[name] = 0
    for Surname in result[name]:
        for Adjustment in result[name][Surname]:
            for cleanName in result[name][Surname][Adjustment]:
                quantity_name[name] += float(result[name][Surname][Adjustment][cleanName]['Estimate'])
top_10 = (sorted(quantity_name.items(), key=lambda t: t[1], reverse=True))[0:10]

names = []
quantity_names = []
for element in top_10:
    names.append(element[0])
    quantity_names.append(element[1])
pl.plot([go.Bar(x=names,y=quantity_names)])
print(top_10)

