def day5_part1(data_list):
    pass


def main():
    with open("input.txt", "r") as file:
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
           
                printing_order = [int(number) for number in line.strip("\n").split(",")]
                new_list = printing_order.copy()[::-1]
                

                score_len = len(printing_order)
            
                for number in new_list:
                    
                    try:
                        aux = [number_val for number_val in new_list[new_list.index(number)+1:] if number_val in before_rules[number]]
                        
                        if (aux == []):
                            score_len -= 1
                            pass
                        else: 
                            
                            break
                    except:
                        score_len -=1
                    
                if score_len == 0:
                    valid_prints.append(printing_order) 
        print(valid_prints)
        media = 0
        for x in valid_prints:
            media += x[len(x)//2]
        print(media)


  


if __name__ == "__main__":
    main()
