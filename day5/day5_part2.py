def is_valid(line, before_rules, toBeAdded):
    print("The toBeAdded is ", toBeAdded, "and the line is ", line)
    printing_order = [int(number) for number in line.strip("\n").split(",")]
    print("printing order: ", printing_order)
    new_list = printing_order.copy()[::-1]
    
    score_len = len(printing_order)

    for number in new_list:
        try:
            aux = [number_val for number_val in new_list[new_list.index(number)+1:] if number_val in before_rules[number]]
            
            if (aux == []):
                score_len -= 1
                pass
            else:
                fix_incorrect(printing_order, before_rules)
                return 
        except:
            score_len -=1
    

    if score_len == 0 and toBeAdded:
        print("It will add this line", printing_order)
        return printing_order
    else:
        return

def fix_incorrect(incorrect, before_rules):
    print("before rules: ", before_rules)
    invert_incorrect = incorrect.copy()[::-1]
    print("incorrect list: ", incorrect)
    for number in invert_incorrect:
        print(number)
        aux = [number_val for number_val in invert_incorrect[invert_incorrect.index(number)+1:] if number_val in before_rules[number]]
        if aux != []:
            print("lets swap ", incorrect[incorrect.index(number)], "and ", incorrect[incorrect.index(aux[0])])
            incorrect[incorrect.index(number)], incorrect[incorrect.index(aux[0])] = incorrect[incorrect.index(aux[0])], incorrect[incorrect.index(number)]
            is_valid(incorrect,before_rules,True)


def main():
    with open("small_input.txt", "r") as file:
        rulesBoolean = True
        before_rules = {}
        valid_prints = []
        
        for line in file:
            if rulesBoolean:
                if(line == "\n"):
                    rulesBoolean = False
                else:
                    aux = line.strip("\n").split("|")
                    try:
                        before_rules[int(aux[0])].append(int(aux[1]))
                    except:
                        before_rules[int(aux[0])] = [int(aux[1])]
            else:
                valid_prints.append(is_valid(line,before_rules,False))
        
        
        print(valid_prints)
        
        
        
        """ media = 0
        for x in valid_prints:
            media += x[len(x)//2] """
       


  


if __name__ == "__main__":
    main()
