#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum
import re 

#A class for comparison operators
class Comparator(Enum):
    Equals = 1
    Less_Than = 0
    Greater_Than = 2

#A method to check if a variable is an integer 
def isVariableANumber(variable):

    answer = True
    try:
        int(variable)
    except:
        answer = False

    return answer

#Converts Version Input to a standard format if necessary : X.X.X.X
def versionFormatConverter(versionString):
    
    newVersionString = ''
    #Check if version input is a simple integer or a decimal number
    try:
        versionString = float(versionString)
        if(versionString < 0):
            print("Version Input : "+ str(versionString) +" is not valid: Only a positive value is supported as version value")
            #Default Value for invalid version set as -1
            newVersionString =  str(-1) 
        else:
            newVersionString =  str(versionString)+"."+"0"+"."+"0"
    #If not, convert version to a standard format
    except:
        #Transform this version format: X.X.X
        if(doesVersionMatch(versionString,re.compile(r"(\d+\.)?(\d+\.)?(\d+)"))):
            newVersionString = str(versionString)+"."+"0"
        #Transform this version format: X.X.X.X
        elif(doesVersionMatch(versionString,re.compile(r"(\d+\.)?(\d+\.)?(\d+\.)?(\d+)"))):
            newVersionString = str(versionString)
        #Alpha Versions Format: X.X-aX
        elif(doesVersionMatch(versionString,re.compile(r"(\d+\.\d+\-a)?(\d*)"))):
            if(isVariableANumber(versionString[-1])):
                temporary_Array = versionString.split("-")
                temporary_Array[1] = temporary_Array[1].replace("a","")
                newVersionString =  str(temporary_Array[0])+"."+"0"+"."+str(temporary_Array[1])
            else:
                temporary_Array = versionString.split("-")
                newVersionString =  str(temporary_Array[0])+"."+"0"+"."+"0"
        #Beta Versions Format: X.X-bX
        elif(doesVersionMatch(versionString,re.compile(r"(\d+\.\d+\-b)?(\d*)"))):
            if(isVariableANumber(versionString[-1])):
                temporary_Array = versionString.split("-")
                temporary_Array[1] = temporary_Array[1].replace("b","")
                newVersionString =  str(temporary_Array[0])+"."+"1"+"."+str(temporary_Array[1])
            else:
                temporary_Array = versionString.split("-")
                newVersionString =  str(temporary_Array[0])+"."+"1"+"."+"0"
        #Release candidates Versions Format: X.X-rcX
        elif(doesVersionMatch(versionString,re.compile(r"(\d+\.\d+\-rc)?(\d*)"))):
            if(isVariableANumber(versionString[-1])):
                temporary_Array = versionString.split("-")
                temporary_Array[1] = temporary_Array[1].replace("rc","")
                newVersionString =  str(temporary_Array[0])+"."+"2"+"."+str(temporary_Array[1])
            else:
                temporary_Array = versionString.split("-")
                newVersionString =  str(temporary_Array[0])+"."+"2"+"."+"0"
        #Commercial distributions Format: X.X-rX
        elif(doesVersionMatch(versionString,re.compile(r"(\d+\.\d+\-r)?(\d*)"))):
            if(isVariableANumber(versionString[-1])):
                temporary_Array = versionString.split("-")
                temporary_Array[1] = temporary_Array[1].replace("r","")
                newVersionString =  str(temporary_Array[0])+"."+"3"+"."+str(temporary_Array[1])
            else:
                temporary_Array = versionString.split("-")
                newVersionString =  str(temporary_Array[0])+"."+"3"+"."+"0"
        else:
            print("Version Input : "+ str(versionString) +" is not valid")
            #Default Value for invalid version set as -1
            newVersionString =  str(-1)
            
    #Return new standard Format version
    return newVersionString

#Check if a version input matches a pattern provided
def doesVersionMatch(versionString,pattern):
    
    answer = True

    matching = re.fullmatch(pattern, str(versionString))
    if(matching):
        newVersionString = str(matching.group())
        if(len(newVersionString) != len(versionString)):
            answer = False
    else:
        answer = False

    return answer

#Compare version inputs:
def versionComparator(version1, version2): 
    #Default Return Value
    valueToReturn = None
    #convert version input to standard format
    version1 = versionFormatConverter(version1)
    if(version1 != str(-1)):
        #convert version input to standard format
        version2 = versionFormatConverter(version2)
        if(version2 != str(-1)):
            
            # This will split both the versions by '.' 
            splittedArray1 = version1.split(".") 
            splittedArray2 = version2.split(".") 
  
            # Initializer for the version inputs arrays 
            arrayIndex = 0 
            

            # The converted version inputs are of the same lenght
            while(arrayIndex < len(splittedArray1)): 
              
                # Version 2 is greater than version 1 
                if(int(splittedArray2[arrayIndex]) > int(splittedArray1[arrayIndex])): 
                    valueToReturn = Comparator.Less_Than.value
                    break          
                # Version 1 is greater than version 2 
                elif(int(splittedArray1[arrayIndex]) > int(splittedArray2[arrayIndex])): 
                    valueToReturn = Comparator.Greater_Than.value
                    break
                #We keep on checking (the values at this index for both version arrays are equal)
                else:
                    arrayIndex += 1  
            #If valueToReturn is still None, Version1 is equal to Version 2 
            if(valueToReturn is None):
                valueToReturn = Comparator.Equals.value
               
    return valueToReturn
