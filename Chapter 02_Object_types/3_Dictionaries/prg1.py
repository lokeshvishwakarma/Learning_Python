#!/usr/bin/python

#Title: Mapping Operation

'''Dictionaries are not sequences, but rather known as mappings.
They store objects by key instead of relative offset
They map keys to values.'''

D={'food':'spam', 'quantity':6,'color':'pink'}
print(D)
print(D['food'])			#fetch value of key "food"
print('quantity: ',D['quantity'])	#fetch value of key "quantity"
D['quantity'] += 1           # Add 1 to 'quantity' value
print('quantity: ',D['quantity'])	#fetch value of key "quantity"


