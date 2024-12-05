


def main(a, b):
    a.sort()
    b.sort()
    total = 0
    for i in range(len(a)):
        total += abs(a[i] - b[i])

    return total

def similarity(a, b):
    total = 0
    for number in a:
        countOccurences = b.count(number)
        score = number * countOccurences
        total += score

    return total


if __name__ == "__main__":
    a = []
    b = []
    with open("input1.txt", "r") as file:
        for line in file:
            aux = line.split()
            a.append(int(aux[0]))
            b.append(int(aux[1]))
 
    print(main(a, b))
    print(similarity(a, b))
