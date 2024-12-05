def checker(number_before, number):
    check1 = abs(number_before - number) <= 3
    check2 = abs(number_before - number) >=1
    return check1 and check2


def main():
    with open("input.txt", "r") as file:
        safeReports = 0

        for line in file:
            aux_line = line.split()
            line = [int(number) for number in aux_line]
            # print(line)
            number_before = line[0]
            isIncresing = False
            isSafe = 1
            errorLimit = 1

            if line[0] < line[1]:
                isIncresing = True
            # print("Crescente" if isIncresing else "Decrescente")

            for i in range(len(line)):
                alreadyDefined = False
                if i != 0:
                    number = line[i]
                    # print("------------")
                    # print("Anterior", number_before)
                    # print("O de Agora", number)
                    
                    if isIncresing and number_before < number:
                        if checker(number_before, number):
                            number_before = number
                        else:
                            errorLimit -= 1
                            print("Um erro feito!", errorLimit)
                            print(line, "\n o i é:", i)
                            if errorLimit < 0:
                                isSafe = 0
                                break

                    elif not isIncresing and number_before > number:
                        if checker(number_before, number):
                            number_before = number
                        else:
                            errorLimit -= 1
                            print("Um erro feito!", errorLimit)
                            print(line, "\n o i é:", i)
                            if errorLimit < 0:
                                isSafe = 0
                                break
                    else:
                        errorLimit -= 1
                        print("Um erro feito!", errorLimit)
                        print(line, "\n o i é:", i)
                        if errorLimit < 0:
                            isSafe = 0
                            break
                        else:
                            print("Entrou aqui com o i", i)
                            if line[i-2] < line[i]:
                                isIncresing = True
                            else:
                                isIncresing = False
                        number_before = number
                        
                        
                
            safeReports += isSafe
            print(safeReports)
        return safeReports

if __name__ == "__main__":
    print(main())
