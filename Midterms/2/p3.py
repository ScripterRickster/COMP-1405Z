def same_character_set(word1, word2):
    """Return True when word1 and word2 contain the same distinct characters."""
    # Write your solution here.
    dict1,dict2 = {},{}

    distinct = True
    for l in word1:
        if l not in dict1:
            dict1[l] = 1

    for l in word2:
        if l not in dict2:
            dict2[l] = 1

    for l in dict1:
        if not l in dict2:
            distinct = False
            break

    if distinct:
        for l in dict2:
            if not l in dict1:
                distinct = False
                break

    return distinct
