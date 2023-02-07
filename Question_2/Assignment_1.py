import csv
import cardinality
import pandas as pd


"""
Question 2.1
"""
def cardinality_items():
  
  def readfile():
    with open('basket_data.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
          print(', '.join(row))

  cardinality.count(readfile())

"""
KN: This code does not run as it appears cardinality is undefined. 

The following error is produced

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-4ea768b924e6> in <module>
     13   cardinality.count(readfile())
     14 
---> 15 cardinality_items()

<ipython-input-3-4ea768b924e6> in cardinality_items()
     11           print(', '.join(row))
     12 
---> 13   cardinality.count(readfile())
     14 
     15 cardinality_items()

NameError: name 'cardinality' is not defined

"""
  
  
"""
Question 2.2
"""
2^N - 1


"""
Question 2.3
"""
def all_itemsets(filename):
  filename = pd.read_csv('basket_data.csv')
  L = filename.nunique()
  return L

"""
KN - 

This code will not run.

Confused by the syntax here. You're taking in a filename as an argument, yet not ever
using it. Pandas read_csv will *not* work, since the length of each line may have
different number of elements. The solution here is a dynamic programming:

def all_itemsets(filename)
  lines = open('basket_data.csv').readlines()
  
  # Return the unique set of items
  unique_items = {}
  for line in lines:
    data = line.split(',')
    for item in data:
      unique_items.add(data)
  
  # Get the permutation of items
  subsets = []
  for item in unique_items:
    new_sets = []
    for unique_set in subsets:
      new_sets.append(unique_set + [item])
    subsets.extend(new_sets)
  subsets.pop(0)
  
  return subsets
"""


"""
Question 2.4
"""
def prob_S(S, D):
    if type(S) is list:
      set_s = set(S)
      len_s = len(set_s)
    else:
      len_s = len(S)
    
    if type(D) is list:
      set_d = set(tuple(d) for d in D)
      len_d = len(set_d)
    else:
      len_d = len(d for d in D)
    
    result = len_s/len_d
    return result
  
"""
KN

This code runs but produces incorrect results. There should be a for loop in here, checking to 
see whether or not each row in D contains all elements of S. Right now, you're only checking
lengths of the data.
"""
