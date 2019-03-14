#!/usr/bin/python
# -*- coding: utf-8 -*-

from QaMethods import *

#Main
print("\nWelcome to Question A's program \n")

#Default variable for the statement to determine
DoLinesOverlap = False

#Get the Points inputs from the User
try:
 
    line1_X1 = float(input('Please enter point 1 position for line 1: \n'))
    line1_X2 = float(input('Please enter point 2 position for line 1: \n'))
    #If positions inputs are valid and form a line, proceed
    if(isLineValid(line1_X1,line1_X2)):
        line2_X1 = float(input('Please enter point 1 position for line 2: \n'))
        line2_X2 = float(input('Please enter point 2 position for line 2: \n'))

#Invalid inputs format
except:
    print("Point must be an integer or a decimal number. The Program can not proceed.\n")

#Set if last variable is defined
isLastInputDefined = True
#Check the last variable to be input: line2_X2
try: 
    line2_X2
except NameError: 
    isLastInputDefined = False

#if coordinates are int or float and form 2 lines, we proceed with the program
if((isLastInputDefined) and (isLineValid(line2_X1,line2_X2))):

    line1 = [line1_X1,line1_X2]
    line2 = [line2_X1,line2_X2]
    
    #Making sure the X1 and X2 positions for each line respectively correspond to the lowest position
    #And the highest position, if not, their values are swapped
    line1 = verifyLineCoordinates(line1)
    line2 = verifyLineCoordinates(line2)

    #Verify if Lines Overlap
    for position in line1:
        if(isValueInInterval(position,line2[0],line2[1])):
            print("Lines Overlap")
            DoLinesOverlap = True
            break
    for position in line2:
        if((isValueInInterval(position,line1[0],line1[1])) and (not DoLinesOverlap)):
            print("Lines Overlap")
            DoLinesOverlap = True
            break

    if(not DoLinesOverlap):
        print("Lines Do not Overlap")

