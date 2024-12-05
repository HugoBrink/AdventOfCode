

def checkNextLetter(letter,next_letter,tries, isValid, total_words, direction):
    print("-----------------\nThe direction is:", direction)
    print("The letter is:", letter, "and the next letter is:", next_letter, "and the tries are:", tries, "and the isValid is:", isValid)
    if letter == "X" and tries == 0:
        if next_letter == "M":
            tries += 1
            isValid = True
            return {"tries": tries, "total": 0, "isValid": isValid}
    elif letter == "M" and tries == 1:
        if next_letter == "A":
            tries += 1
            isValid = True
            return {"tries": tries, "total": 0, "isValid": isValid}
    elif letter == "A" and tries == 2:
        if next_letter == "S":
            tries += 1
            isValid = True
            return {"tries": tries, "total": 0, "isValid": isValid}
    elif letter == "S" and tries == 3:
        tries = 0
        isValid = True
        return {"tries": tries, "total": 1, "isValid": isValid}
    print("is not valid")
    isValid = False
    tries = 0
    return {"tries": tries, "total": 0, "isValid": isValid}

def main():
    valid_letters = ["X", "M", "A", "S"]
    total_words = 0
    with open("small_input.txt", "r") as file:
        data = file.read()
        data_list = data.split("\n")
        new_list = []
        for chunk_letters in data_list:
            new_line = []
            for single_letter in chunk_letters:
                new_line.append(single_letter)
            new_list.append(new_line)

        print(new_list)
        for i in range(len(new_list)):
            triesHorizontal = 0
            isValidHorizontal = False
            triesVertical = 0
            isValidVertical = False
            for j in range(len(new_list[i])):
                if new_list[i][j] in valid_letters:
                    # Horizontal check
                    if new_list[i][j] == "X":
                        isValidHorizontal = True
                    while(isValidHorizontal):
                        print(new_list[i][j])
                        try:
                            result = checkNextLetter(new_list[i][j], new_list[i][j+1], triesHorizontal, isValidHorizontal, total_words, "Horizontal")
                            triesHorizontal = result["tries"]
                            total_words += result["total"]
                            isValidHorizontal = result["isValid"]
                        except:
                            print("Letter", new_list[i][j], "is the first letter of a word")
                            result = checkNextLetter(new_list[i][j], 0, triesHorizontal, isValidHorizontal, total_words, "Horizontal")
                            triesHorizontal = result["tries"]
                            total_words += result["total"]
                            isValidHorizontal = result["isValid"]
                    # Vertical check
                    if new_list[i][j] == "X":
                        isValidVertical = True
                    if isValidVertical:
                        print(new_list[i][j])
                        try:
                            result = checkNextLetter(new_list[i][j], new_list[i+1][j], triesVertical, isValidVertical, total_words, "Vertical")
                            triesVertical = result["tries"]
                            total_words += result["total"]
                            isValidVertical = result["isValid"]
                        except:
                            print("Letter", new_list[i][j], "is the first letter of a word")
                            result = checkNextLetter(new_list[i][j], 0, triesVertical, isValidVertical, total_words, "Vertical")
                            triesVertical = result["tries"]
                            total_words += result["total"]
                            isValidVertical = result["isValid"]

        print(total_words)


if __name__ == "__main__":
    main()
