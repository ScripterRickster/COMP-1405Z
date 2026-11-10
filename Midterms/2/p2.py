def find_single_repeat_words(S):
    """Return qualifying words as described in Problem 2."""
    # Write your solution here.

    S = S.split()

    valid_words = []

    for w in S:
        letter_dict = {}
        w = w.lower().strip()

        for l in w:
            if not l in letter_dict:
                letter_dict[l] = 1
            else:
                letter_dict[l] += 1

        has_two = False
        for l in letter_dict:
            if letter_dict[l] >= 2:
                if not has_two:
                    has_two = True
                else:
                    has_two = False
                    break


        if has_two and w not in valid_words: 
            valid_words.append(w)

    return valid_words