names = ["Doe, John", "White, Mary", "Toth, Colin", "Stone, Bob"]

def rearrangeNames(namesArray, separator):
    rearrangedArray = []
    for name in namesArray:
        firstAndLastName = name.split(separator)
        firstName = firstAndLastName[1]
        lastName = firstAndLastName[0]
        rearrangedArray.append(firstName + " " + lastName)
    return rearrangedArray


print("BEFORE: " + str(names))
rearrangedNames = rearrangeNames(names, ", ")
print("AFTER: " + str(rearrangedNames))
