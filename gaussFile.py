#!/usr/bin/env python3
import pathlib
filepath = pathlib.Path(__file__).resolve().parent   #get the path of the program
f = open(str(filepath)+"\\matrix.txt")                  #txt file must be in the same folder as gaussFile.py
lines = f.readlines()                             #list of each line as strings

A = []
for i in range(len(lines)):
    temp = []                           #reset temp
    line = lines[i].split(" ")          #line is a list of each value separated by spaces on one line
    for j in range(len(line)):
        temp.append(float(line[j]))       #temp becomes a copy of line but cast as floats
    A.append(temp)                      
# A = [[1, 2, 3, 4],
#      [3, 0, 2, 1],
#      [2,-1, 5, 1]]

num_rows = len(A)
num_cols = len(A[0])
goodFormat = True
for i in range(num_rows):
    if(len(A[i]!=num_cols)):
        goodFormat = False              #make sure all rows are same size
if(goodFormat):
    for k in range(0, num_rows-1):  # row being used
        for i in range(k+1, num_rows):  # row being changed
            pivot_mult = A[i][k]/A[k][k]
            for j in range(0, num_cols):  # column number in that row
                A[i][j] =  A[i][j] - pivot_mult*A[k][j]
    print("solution is: ",A)
else:
    print("not all rows are the same size")