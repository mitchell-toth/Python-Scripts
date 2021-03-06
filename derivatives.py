def parsePower(term,index):
    endIndex = index
    for charIndex in range(index,len(term)):
        if term[charIndex] not in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
            break
        endIndex += 1
    power = term[index:endIndex]
    return power


def parseTerm(term):
    coefficient = ""
    variable = ""
    power = 1
    powerLength = 0
    for charIndex in range(len(term)):
        if powerLength > 0:
            powerLength -= 1
            continue
        if term[charIndex] in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
            coefficient += term[charIndex]
        elif term[charIndex] in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            variable = term[charIndex]
        elif term[charIndex] == "^":
            power = parsePower(term,charIndex+1)
            powerLength = len(power)
    if coefficient == "":
        coefficient = 1
    return coefficient, variable, power
                

def derivativeOfLn(term):
    coefficient = term[0]
    variable = term[1]
    return ("1/(" + str(coefficient) + str(variable) + ")")


def displayParsedData(term, coefficient, variable, power):
    print("Term: " + term)
    print()
    print("Coefficient = " + coefficient)
    print("Variable = " + variable)
    print("Power = " + power)
    print()


def derivativeOf(term):
    coefficient, variable, power = parseTerm(term)
    #displayParsedData(term, coefficient, variable, power)
    newCoefficient = float(coefficient) * float(power)
    newPower = float(power)-1
    if newPower == 1.0:
        derivativeTerm = str(newCoefficient)+variable
    else:
        derivativeTerm = str(newCoefficient)+variable+"^"+str(newPower)
    print("TERM = " + term)
    print("DERIVATIVE = " + derivativeTerm)
    
        
#derivativeOf("9.2x^2")



#--Sorting algorithm exercise--
def sortList(numberList):
    doItTheLongWay = True
    unsortedList = numberList
    sortedList = []
    
    for i in range(len(numberList)):
        #Find minimum number in unsortedList and its index
        if doItTheLongWay == True:
            minNumber = 999999
            minNumberIdx = 0
            for idx in range(len(unsortedList)):
                if unsortedList[idx] < minNumber:
                    minNumber = unsortedList[idx]
                    minNumberIdx = idx
        else:
            minNumberIdx = unsortedList.index(min(unsortedList))

        #Append to sortedList and remove from unsortedList
        sortedList.append(unsortedList[minNumberIdx])
        unsortedList.pop(minNumberIdx)
    return sortedList
        
        

numbers = [6,3,8,1,2,2,5,3,7,9,4,9,1,6,4,1,7]
numbers = sortList(numbers)
print(numbers)

