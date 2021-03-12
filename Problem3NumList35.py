#Kerem Kok
#3/10/21
#Problem 3. Asking the user to enter a number and entering each number to a list until their sum adds up to 100. 

numbers = [] #creating the list
grandTotal = 0
while grandTotal <= 100:
    prompt = "Your total is " + str(grandTotal) + ". Please enter a number to add: "
    userInput = int(input(prompt))
    numbers.append(userInput)
    grandTotal = 0
    for num in numbers:
        grandTotal = grandTotal + num
