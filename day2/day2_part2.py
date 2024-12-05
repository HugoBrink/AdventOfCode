def checker(number_before, number):
    check1 = abs(number_before - number) <= 3
    check2 = abs(number_before - number) >=1
    return check1 and check2

def isSafe(line):
    number_before = line[0]

    isIncresing = False
    isSafe = 1

    if line[0] < line[1]:
        isIncresing = True

    for i in range(len(line)):
        alreadyDefined = False
            
        if i != 0:
            number = line[i]
            
            if isIncresing and number_before < number:
                if checker(number_before, number):
                    number_before = number
                else:
                    isSafe = 0
                    return 0

            elif not isIncresing and number_before > number:
                if checker(number_before, number):
                    number_before = number
                else:
                    isSafe = 0
                    return 0
            else:
                isSafe = 0
                return 0
                
            number_before = number
    return 1


def main():
    with open("input.txt", "r") as file:
        safeReports = 0

        for line in file:
            aux_line = line.split()
            line = [int(number) for number in aux_line]
   
            reportIsSafe = isSafe(line)
            i = 0
            while reportIsSafe == 0 and i < len(line):
                new_line = line.copy()
                new_line.pop(i)
                reportIsSafe = isSafe(new_line)
                i += 1
            safeReports += reportIsSafe
        return safeReports


if __name__ == "__main__":
    print(main())



