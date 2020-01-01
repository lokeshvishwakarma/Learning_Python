#!/usr/bin/python

# Title: Missing Keys: if Tests

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D['e'] = 99  # Assigning new keys grows dictionaries
print(D)
# print(D['f'])  # Referencing a non existent key is an error

if not 'f' in D:  # check if key 'f' not in D
    print('Missing key "f"')

print(D.get('b'))

if 'b' in D:
    print('Found')
else:
    print('Missing')
print(D.keys())

for k, v in D.items():
    print(k, v)

l1 = ['name', 'job', 'age']
l2 = ['Loki', 'Developer', 23]

Z = {}
for k in l1:
    for v in l2:
        Z.setdefault(k, v)

print(Z)
