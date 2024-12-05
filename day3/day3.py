import re


def mul(a,b):
	return a*b


def main():
    with open("input.txt", "r") as file:
        data = file.read()
        mul_list = re.findall(r"mul\([0-9]{0,3},[0-9]{0,3}\)|don't\(\)|do\(\)", data)
        total = 0
        stop = False
        for mul_element in mul_list:
            if mul_element == "do()":
                stop = False
            elif mul_element == "don't()":
                stop = True
            else:
                multipliers = re.findall(r"[0-9]{0,3},[0-9]{0,3}",mul_element)[0].split(",")
                if not stop:
                    total += mul(int(multipliers[0]),int(multipliers[1]))
                else:
                    pass
            

        print(total)


if __name__ == "__main__":
    main()