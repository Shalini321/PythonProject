# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently search for a target 
# value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm to find a target value 
# in a sorted list?


##-------------------------------------------------------------------------------------------
##----------- Date 29 May,2025, Written By - Shalini Singh  ---------------------------------
##-------------------------------------------------------------------------------------------

# Function to get middle index and number at middle index.
def findMidItem (itemList,firstIndex,lastIndex):   
    midIndex= int(firstIndex + (lastIndex-firstIndex)/2)
    midItem=itemList[midIndex]
    return midIndex,midItem

# Arraye/List of shorted numbers
items = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
#items= range(0,100)  # for testing

# Search for target number from array/list
targetNum = 20
# Call function to find the middle item of array/list
try:
    firstIndex = 0
    lastindex = len(items)-1
    midIndex,midItem = findMidItem(items,firstIndex,lastindex)

    while targetNum != midItem :
         if targetNum > midItem :
            firstIndex = midIndex
            lastindex = lastindex
            midIndex, midItem=findMidItem (items,firstIndex,lastindex)
            continue
         else :
            firstIndex = firstIndex
            lastindex = midIndex
            midIndex, midItem=findMidItem (items,firstIndex,lastindex)
            continue
    else :
        print(f"Result : {targetNum},is at index : {midIndex} ")
        
except ValueError as err:
        print("Error : ", err)
    
#---------------------- End of the Program ------------------------------------