# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:26:44 2023
QUESTION: A2Q2
@author: Haryish Elangumaran
"""

def rotate_matrix(matrix, rotation):
    """Function to rotate the matrix by 90, 180, 270, or 360 degrees."""
    rows = len(matrix)
    cols = len(matrix[0])
    rotated_matrix = []

    #rotates matrix to 90 degree
    if rotation == 90:
        for j in range(cols):
            row = []
            for i in range(rows - 1, -1, -1):
                row.append(matrix[i][j])
            rotated_matrix.append(row)

    #rotates matrix to 180 degree
    elif rotation == 180:
        for i in range(rows - 1, -1, -1):
            rotated_matrix.append(matrix[i][::-1])

    #rotates matrix to 270 degree
    elif rotation == 270:
        for j in range(cols - 1, -1, -1):
            row = []
            for i in range(rows):
                row.append(matrix[i][j])
            rotated_matrix.append(row)

    #Rotates batrix to 360 degree        
    elif rotation == 360:
        rotated_matrix = matrix

    return rotated_matrix

#To print the resultant matrix
def print_matrix(matrix):
    """Function to print the matrix in a user-friendly way."""
    for row in matrix:
        print(row)
    print("\n")

#Prescribing the matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Given Matrix:")
print_matrix(matrix)

#Menu list
print("Matrix Rotation Menu\n  1. Rotate by 90 degrees\n  2. Rotate by 180 degrees\n  3. Rotate by 270 degrees\n  4. Rotate by 360 degrees\n  5. Exit\n")

#Processing the options
while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        matrix = rotate_matrix(matrix, 90)
        print_matrix(matrix)
    elif choice == 2:
        matrix = rotate_matrix(matrix, 180)
        print_matrix(matrix)
    elif choice == 3:
        matrix = rotate_matrix(matrix, 270)
        print_matrix(matrix)
    elif choice == 4:
        matrix = rotate_matrix(matrix, 360)
        print_matrix(matrix)
    elif choice == 5:
        print("closed")
        break
    else:
        print("Invalid choice. Please try again.")
