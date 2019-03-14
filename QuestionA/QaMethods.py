#!/usr/bin/python
# -*- coding: utf-8 -*-

#Verify if the two positions provided form a line
def isLineValid(line_X1,line_X2):
    
    answer = True

    if(line_X1 == line_X2):
        answer = False
        print("Points coordinates must be different from each other to form a line")
    
    return answer

#Verify if the two positions provided form respectively the lower bound and the upper bound of #the line
def verifyLineCoordinates(line):

    line_X1 = line[0]
    line_X2 = line[1]

    #Swap the line's bounds
    if(line_X1 > line_X2):
        temporary_point = line_X1
        line_X1 = line_X2
        line_X2 = temporary_point
        print("Line Coordinates\' bounds have been swapped from X1 = "+str(line_X2)+" and X2 = "+str(line_X1)+ "\n Line is now: ("+str(line_X1)+","+str(line_X2)+")")

    line = [line_X1,line_X2]
    
    return line

#Check if a position bound belongs to a line interval (represented by its bounds)
def isValueInInterval(value,lower_bound,upper_bound):
    
    answer = False

    if((lower_bound<=value) and (upper_bound>=value)):
        answer = True

    return answer

