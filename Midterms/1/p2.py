
def count_numbers(nList):
    if nList == "": return 0
    if len(nList) > 0 and nList.count(" ") == 0: return 1
    return nList.count(" ") + 1

def analyze(filename):
    file = open(filename,"r")

    numlist = ""
    longest = 0

    for line in file:
        num = int(line.strip())
        if num % 2 == 1:
            numlist = numlist + (line.strip())
            while num % 2 == 1:
                newLine = file.readline()
                if not newLine: break
                num = int(newLine.strip())
                if num % 2 == 1:
                    numlist = numlist + " " + (newLine.strip())
            if count_numbers(numlist) > longest:
                longest = count_numbers(numlist)

            numlist = ""

    
    if count_numbers(numlist) > longest:
        longest = count_numbers(numlist)

    return longest
