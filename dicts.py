x = { 'first':1, 'second':2 }
print(x['first'])
x = dict([('first', 1), ('second', 2)])
print(x)
x = dict(first = 1, second = 2)
print(x)
x['third'] = 3
print(x)
del(x['third'])
print(x)

for key in x:
    print(key, x[key])

for k, v in x.items():
    print(k, v)

print(x.items())