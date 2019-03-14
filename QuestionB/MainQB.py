#!/usr/bin/python
# -*- coding: utf-8 -*-

from VersionComparisonLibrary import *

#Main
print("\nWelcome to Question B's test program \n")


"""Test Cases
  - Input does not have a software version standard format (X or X.X or X.X.X or X.X.X.X)
  - Input is negative 
  - Version format designating development stage (alpha, beta, release candidate, final release) with the assumption that it is used in the third position (For example: 1.2-a1, 1.2-b2, 1.2-rc3)
  - Input has one of the following formats: (X or X.X or X.X.X or X.X.X.X)
"""
#Get the versions inputs from the User
version1 = input('Please enter version 1\'s value : \n')

version2 = input('Please enter version 2\'s value :  \n')

#Compare versions obtained from the User
result = versionComparator(version1, version2)

if(result == 0): 
    print("Version "+str(version1) + " is smaller than " +"version "+str(version2))
elif(result == 2): 
    print("Version "+str(version1) + " is greater than " +"version "+str(version2))
elif(result == 1): 
    print("The 2 versions are equal")

