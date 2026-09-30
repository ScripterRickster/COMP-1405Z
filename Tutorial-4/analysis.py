# Made By Ricky L.

word_count = {}
all_text = []
def load(filename):
    file = open(filename,'r')

    global word_count,all_text

    all_text = file.read().split()
    file.close()
   
    word_count = {}

    for word in all_text:
        if (word.strip()).lower() not in word_count:
            word_count[(word.strip()).lower()] = 1
        else:
            word_count[(word.strip()).lower()] += 1


def commonword(list):
    if len(list) == 0: return None
    found_word = False
    for word in list:
        if (word.strip()).lower() in word_count:
            found_word = True
            break
    if not found_word: return None

    word_freq = {}
    max_freq,max_word = 0,0
    for word in list:
        if (word.strip()).lower() in word_count:
            word_freq[(word.strip()).lower()] = word_count[(word.strip()).lower()]

            if word_freq[(word.strip()).lower()] > max_freq:
                max_freq = word_freq[(word.strip()).lower()]
                max_word = (word.strip())

    return max_word

def commonpair(str):
    first = str.strip().lower()

    if not first in word_count: return None

    word_pair_dict = {}
    
    for i in range(len(all_text) - 1):
        if all_text[i].strip().lower() == first:
            following = all_text[i + 1].strip().lower()
            if following in word_pair_dict:
                word_pair_dict[following] += 1
            else:
                word_pair_dict[following] = 1

    if len(word_pair_dict) == 0:
        return None

    common_word = None
    common_count = 0
    for word in word_pair_dict:
        if word_pair_dict[word] > common_count:
            common_word = word
            common_count = word_pair_dict[word]

    return common_word


def countall():
    return len(all_text)

def countunique():
    return len(word_count)


    
