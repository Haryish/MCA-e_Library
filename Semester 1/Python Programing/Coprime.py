# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:13:43 2023
QUESTION: A1Q3
@author: Haryish Elangumaran
"""


def coprimenumber(a, b):
  x = set(factors(a))
  y = set(factors(b))
  hcf = x.intersection(y)
  print("The common factor of {} and {} is {}".format(a,b,hcf))
  if hcf == {1}:
    print('{} and {} are coprime'.format(a, b))
  else:
    print('{} and {} are not coprime'.format(a, b))


def factors(number):
  factor = [1]
  for j in range(2, number + 1):
    if number % j == 0:
      factor.append(j)
  return factor

a,b=14,15
print("Inputs: {},{}".format(a,b))
print("Factor of {} is {} and {}".format(a,factors(a)[:len(factors(a))-1],factors(a)[len(factors(a))-1]))
print("Factor of {} is {} and {}".format(b,factors(b)[:len(factors(b))-1],factors(b)[len(factors(b))-1]))
coprimenumber(a,b)