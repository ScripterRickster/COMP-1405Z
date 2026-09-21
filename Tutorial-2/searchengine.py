'''

Made By Ricky L.

'''



def get_pages():
    f = open("pages.txt","r")

    pages = []
    for l in f:
        pages.append(l.strip())

    f.close()
    return pages

def get_word_count(filename,word):
    if not filename or not word: return 0

    f = open(filename,"r")

    count = 0
    for l in f:
        if l.strip().lower() == word.lower():
            count += 1

    f.close()
    return count

def get_word_ratio(filename,word):
    if not filename or not word: return 0

    f = open(filename,"r")

    count = 0
    totalwords = 0
    for l in f:
        totalwords += 1
        if l.strip().lower() == word.lower():
            count += 1

    f.close()
    if totalwords == 0: return 0
    return count/totalwords


word = input("Enter a word to search for: ")


mpagec = ""
mcount = 0
mpager = ""
mratio = 0.0



for p in get_pages():
    count = get_word_count(p,word)
    if count > mcount:
        mcount = count
        mpagec = p

    ratio = get_word_ratio(p,word)
    if ratio > mratio:
        mratio = ratio
        mpager = p


print(f"\nMax Count: {mpagec}\nMax Ratio: {mpager}")
    




