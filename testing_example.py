
studentTripExpenses = {}

def dictCreate(studentAmount): #studentAmount is the number of students.
    for i in range(0, studentAmount):
        studentName = input("What is the name of the student? ")
        expenseList = []
        print("Enter 'done' to move to the next student.")
        while True:
            expense = input("What is the cost of this expense? ")
            if expense.lower() == 'done':
                break
            elif (float(expense) >= 0) or (float(expense) < 0):
                expenseList.append(float(expense))
            elif not expense.isdigit():
                print("Please enter a number or enter 'done' to move on.")
        studentTripExpenses[studentName] = expenseList
    return studentTripExpenses

def studentCost(dct):
    #
    for i in dct:
        #Variable for individual costs of student
        personalCost = 0
        #Determines the total cost for each student
        for x in dct[i]:
            personalCost = personalCost + x
        #Sets each students value to their total cost to two decimal places
        dct[i] = float("%.2f" % personalCost)
    return dct

def amountsDue(expenseLst, studentAvgPrice):
        #Runs through the dictionary of students and individual total trip costs
        for key in expenseLst:
            maxPerson = max(expenseLst, key=expenseLst.get)
            costDifference = 0
            #Determines who owes who how much money
            if max(expenseLst.values()) >= expenseLst[key]:
                costDifference = studentAvgPrice-expenseLst[key]
                if (costDifference < 0):
                    costDifference = costDifference * -1
                print("%s owes %s $%.2f" % (key, maxPerson, costDifference))

def main():
    numOfStudents = int(input("How many students are going on the trip? ")) #Gets the number of students, like 3
    studentCostDict = dictCreate(numOfStudents) #creates a dictionary like {'John': [5,6,10], 'Sue': [4,6,1], 'Jane': [0,10,5]}
    studentTripExpenses = studentCost(studentCostDict) #Now the dictionary is like {{'John': 21, 'Sue': 11, 'Jane': 15}}

    totalCost = 0

    #Gets the total cost for all students
    for key in (studentTripExpenses):
        totalCost = totalCost + studentTripExpenses[key]

    #Changes the total cost to 2 decimal places
    totalCost = float("%.2f" % totalCost)

    #Determines the average amount spent per student
    avgCost = float("%.2f" % (totalCost/len(studentTripExpenses)))

    amountsDue(studentTripExpenses, avgCost) #Whoever has the greatest expense pays upfront, everyone else pays him back.
    #Should say Sue owes John 11, and jane owes john 15.
if __name__=='__main__':
    main()