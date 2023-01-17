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
