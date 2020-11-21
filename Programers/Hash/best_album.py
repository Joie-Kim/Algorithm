dic = {'a':1, 'b':2, 'c':3, 'd':[1,2,3]}

# sort_list = sorted(dic.items(), reverse=True, key=lambda item: item[1])

print(dic['d'])
print(dic.items())
print(dic.values())
print(list(dic.values())[3][0])

dic['d'].append(4)
print(dic['d'])

dic['e'] = 1
dic['e'].append(4)
print(dic['e'])