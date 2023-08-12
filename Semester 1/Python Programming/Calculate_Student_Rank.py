# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:43:05 2023
QUESTION: A1Q2
@author: Haryish Elangumaran
"""
import json #<-- Optional line

def stud_rank(details):
    # iterate over the dictionary to calculate total internal marks for each student
    for key, value in details.items():
        total = sum(value['ass1'].values()) + sum(value['ass2'].values())
        details[key]['imark'] = total

    # sort the dictionary based on total internal marks in ascending order
    sorted_dict = sorted(details.items(), key=lambda x: x[1]['imark'], reverse=True)

    # calculate rank for each student based on the sorted dictionary
    rank = 1
    for key, value in sorted_dict:
        details[key]['rank'] = rank
        rank += 1

    # return the sorted dictionary with updated ranks and internal marks
    return sorted_dict

details = {
  20201010: {
    'name': 'Khan', 'age': 18,
    'ass1': {
      'phy': 88,'chem': 99,'mat': 99, 'py': 99
    },
    'ass2': {
      'phy': 88,'chem': 99,'mat': 99,'py': 99
    },
    'imark': 0,'rank': 0
  },
  20201011: {
    'name': 'Sam','age': 18,
    'ass1': {
      'phy': 81,'chem': 79,'mat': 99,'py': 89
    },
    'ass2': {
      'phy': 80,'chem': 89,'mat': 79,'py': 79
    },
    'imark': 0,'rank': 0
  },
  20201012: {
    'name': 'Ram','age': 18,
    'ass1': {
      'phy': 68,'chem': 79,
      'mat': 89,'py': 99
    },
    'ass2': {
      'phy': 58,'chem': 69,'mat': 79,'py': 99
    },
    'imark': 0,'rank': 0
  }
}

sorted_details=stud_rank(details)
json_sorted_details = json.dumps(sorted_details, indent=4) #<--- Optional line if the output you decire should be in JSON format
print(sorted_details) #<--- To print in Json Format, Place sorted_details with json_sorted_details
