

def checkNextLetter(letter,next_letter):
    #print("letter:", letter, "next_letter:", next_letter)
    if letter == "X":
        if next_letter == "M":
            return True
    elif letter == "M":
        if next_letter == "A":
            return True 
    elif letter == "A": 
        if next_letter == "S":
            return True
    elif letter == "S":
        return True

    return False


#parte 1
def validation(new_list):
    total_words = 0
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            isValid = True
            if new_list[i][j] == "X":
                #print("Horizontal check...")
                # HORIZONTAL CHECK
                k = j
                while(isValid):
                    #print(new_list[i][k], "in row", i, "column", k)
                    if new_list[i][k] == "S":
                        #print("Word Found!")
                        total_words += 1
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[i][k], new_list[i][k+1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k += 1
                #print("Horizontal check done!\n-------------------\nStarting vertical check...")
                #VERTICAL CHECK
                isValid = True
                k=i
                while(isValid):
                    #print(new_list[k][j], "in row", k, "column", j)
                    if new_list[k][j] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][j], new_list[k+1][j])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k += 1
                #print("Vertical check done!\n-------------------\nStarting VERTICAL BACKWARDS check...")

                #VERTICAL BACKWARDS CHECK
                isValid = True
                k=i
                while(isValid):
                    #print(new_list[k][j], "in row", k, "column", j)
                    if new_list[k][j] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][j], new_list[k-1][j])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k -= 1
                    if k < 0:
                        isValid = False
                #print("VERTICAL BACKWARDS check done!\n-------------------\nStarting BACKWARDS check...")
                #BACKWARDS CHECK
                isValid = True
                k=j
                while(isValid):
                    #print(new_list[i][k], "in row", i, "column", k)
                    if new_list[i][k] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[i][k], new_list[i][k-1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k -= 1
                    if k < 0:
                        isValid = False
                #print("Backwards check done!\n-------------------\nStarting diagonal check...")
                #print("Top Left Diagonal check...")
                #DIAGONAL CHECK - TOP LEFT
                isValid = True
                k=i
                m=j
                while(isValid):
                    #print(new_list[k][m], "in row", k, "column", m)
                   
                    if new_list[k][m] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][m], new_list[k-1][m-1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k -= 1
                    m -= 1
                    if k < 0 or m < 0:
                        isValid = False
                #print("Top Left Diagonal check done!\n-------------------\nTop Right Diagonal check...")
                #DIAGONAL CHECK - TOP RIGHT
                isValid = True
                k=i
                m=j
                while(isValid):
                    #print(new_list[k][m], "in row", k, "column", m)
                    if new_list[k][m] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][m], new_list[k-1][m+1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k -= 1
                    m += 1
                    if k < 0:
                        isValid = False
                #print("Top Right Diagonal check done!\n-------------------\nBottom Left Diagonal check...")
                #DIAGONAL CHECK - BOTTOM LEFT
                isValid = True
                k=i
                m=j
                while(isValid):
                    #print(new_list[k][m], "in row", k, "column", m)
                    if new_list[k][m] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][m], new_list[k+1][m-1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k += 1
                    m -= 1
                    if m < 0:
                        isValid = False
                #print("Bottom Left Diagonal check done!\n-------------------\nBottom Right Diagonal check...")
                #DIAGONAL CHECK - BOTTOM RIGHT
                isValid = True
                k=i
                m=j
                while(isValid):
                    #print(new_list[k][m], "in row", k, "column", m)
                    if new_list[k][m] == "S":
                        total_words += 1
                        #print("Word Found!")
                        isValid = False
                    else:
                        try:
                            isValid = checkNextLetter(new_list[k][m], new_list[k+1][m+1])
                        except:
                            #print("No more letters to check")
                            isValid = False
                    k += 1
                    m += 1
                #print("Diagonal check done!\n-------------------\nLetter:", new_list[i][j], " vista.\nTotal words found:", total_words)
    print(total_words)

def positive_number_verification(number):
    if number < 0:
        return False
    return True

#parte 1 simplificadissima (será)

def parte1_simplificada(new_list):
    total_words = 0
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if new_list[i][j] == "X":
                #HORIZONTAL
                try:
                    if new_list[i][j+1] == "M" and new_list[i][j+2] == "A" and new_list[i][j+3] == "S":
                        total_words += 1
                except:
                    pass #out of bounds
                #BACKWARDS
                try:
                    if positive_number_verification(j-1) and positive_number_verification(j-2) and positive_number_verification(j-3):
                        if new_list[i][j-1] == "M" and new_list[i][j-2] == "A" and new_list[i][j-3] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                #VERTICAL
                try:
                    if new_list[i+1][j] == "M" and new_list[i+2][j] == "A" and new_list[i+3][j] == "S":
                        total_words += 1
                except:
                    pass #out of bounds
                #VERTICAL BACKWARDS
                try:
                    if positive_number_verification(i-1) and positive_number_verification(i-2) and positive_number_verification(i-3):
                        if new_list[i-1][j] == "M" and new_list[i-2][j] == "A" and new_list[i-3][j] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                #DIAGONAL TOP LEFT
                try:
                    if positive_number_verification(i-1) and positive_number_verification(j-1) and positive_number_verification(i-2) and positive_number_verification(j-2) and positive_number_verification(i-3) and positive_number_verification(j-3):
                        if new_list[i-1][j-1] == "M" and new_list[i-2][j-2] == "A" and new_list[i-3][j-3] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                #DIAGONAL TOP RIGHT
                try:
                    if positive_number_verification(i-1) and positive_number_verification(i-2) and positive_number_verification(i-3):
                        if new_list[i-1][j+1] == "M" and new_list[i-2][j+2] == "A" and new_list[i-3][j+3] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                #DIAGONAL BOTTOM LEFT
                try:
                    if positive_number_verification(j-1) and positive_number_verification(j-2) and positive_number_verification(j-3):
                        if new_list[i+1][j-1] == "M" and new_list[i+2][j-2] == "A" and new_list[i+3][j-3] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                #DIAGONAL BOTTOM RIGHT
                try:
                    if new_list[i+1][j+1] == "M" and new_list[i+2][j+2] == "A" and new_list[i+3][j+3] == "S":
                        total_words += 1
                except:
                    pass #out of bounds
    print(total_words)

#parte 2
def x_validation(new_list):
    total_words = 0
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if new_list[i][j] == "A":
                try: #CIMA esquerda CIMA direita BAIXO esquerda BAIXO direita
                    if positive_number_verification(i-1) and positive_number_verification(j-1):
                        if new_list[i-1][j-1] == "S" and new_list[i-1][j+1] == "S" and new_list[i+1][j-1] == "M" and new_list[i+1][j+1] == "M":
                            total_words += 1
                except:
                    pass #out of bounds
                try:
                    if positive_number_verification(i-1) and positive_number_verification(j-1):
                        if new_list[i-1][j-1] == "M" and new_list[i-1][j+1] == "S" and new_list[i+1][j-1] == "M" and new_list[i+1][j+1] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                try:
                    if positive_number_verification(i-1) and positive_number_verification(j-1):
                        if new_list[i-1][j-1] == "M" and new_list[i-1][j+1] == "M" and new_list[i+1][j-1] == "S" and new_list[i+1][j+1] == "S":
                            total_words += 1
                except:
                    pass #out of bounds
                try:
                    if positive_number_verification(i-1) and positive_number_verification(j-1):
                        if new_list[i-1][j-1] == "S" and new_list[i-1][j+1] == "M" and new_list[i+1][j-1] == "S" and new_list[i+1][j+1] == "M":
                            total_words += 1
                except:
                    pass #out of bounds
                
    print(total_words)


def main():
    with open("input.txt", "r") as file:
        data = file.read()
        data_list = data.split("\n")
        new_list = []
        for chunk_letters in data_list:
            new_line = []
            for single_letter in chunk_letters:
                new_line.append(single_letter)
            new_list.append(new_line)
        #print(new_list)
        parte1_simplificada(new_list)
        #x_validation(new_list)

if __name__ == "__main__":
    main()
