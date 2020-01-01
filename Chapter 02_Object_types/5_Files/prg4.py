#!/usr/bin/python

# Title: Pickling Files

"""The pickle module is a more advanced tool that allows us to store almost any Python object in a
 file directly."""

import pickle

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)  # Pickle any object to file
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)  # Load any object from fil
print(E)
