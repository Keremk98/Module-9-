#Kerem Kok
#3/10/21
#Problem 4.Creating a while loop that initializes a counter at 0 and runs until the counter reaches 50.  
tens = [] #creating the list called tens
grandTotal = 0
while grandTotal <= 50:
    grandTotal = grandTotal + 1
    if grandTotal % 10 == 0: #if statement for the numbers divisible by ten
        tens.append(grandTotal)
        print( "Current total " + str(grandTotal) + ". The list is ")
        print( tens[0:])
