import random

def get_pairs(keys):
    """
        returns every pair of a given set of keys.
    """
    pairs = []
    for a in keys:
        for b in keys:
            pairs.append(a+b)
    return pairs


def get_r_hand_pairs():
    """
        returns every pair of the right hand keys with punctuation.
    """
    keys = "yuiophjkl'nm,."
    return get_pairs(keys)


def get_r_hand_letter_pairs():
    """
        returns every pair of the right hand keys.
    """
    keys = "yuiophjklnm"
    return get_pairs(keys)


def get_l_hand_letter_pairs():
    """
        returns every pair of the left hand keys.
    """    
    keys = 'qwertasdfgzxcvb'
    return get_pairs(keys)

def get_vitamin_c():
    """
        to fix my major issues with the c key plus bottom row.
    """    
    keys = 'xcvbsdfgwert'
    return get_pairs(keys)

def typist(pairs):
    """
        Returns a string that rolls through every pair of consecutive keys that can be hit.
    """
    random.shuffle(pairs)
    typestring = pairs.pop(0)
    while len(pairs) > 0:
        last_char_string = typestring[-1]
        for i, pair in enumerate(pairs):
            first_char_pair = pair[0]
            if last_char_string == first_char_pair:
                pairs.remove(pair)
                to_add = pair[1]
                typestring = typestring + to_add
                break
            elif i == len(pairs) - 1:
                pairs.remove(pair)
                to_add = pair[1]
                typestring = typestring + to_add
                break
    return typestring


def batch(chars, word_length=5):
    """
        takes a string of chars, and returns it split it into words of length word_length.
        the words overlap by one character, so that no pair of keys for the typing exercise is missed. 
    """
    words = []
    for i in range(0, len(chars), word_length-1):
        hi = min(len(chars), i+word_length)
        word = chars[i:hi]
        if len(word)>1:
            words.append(word)
    return " ".join(words)


# generate the full string that rolls through every pair of keys per hand.
# batch the string into overlapping 5 letter words for the typing test.
left = batch(typist(get_l_hand_letter_pairs()))
right = batch(typist(get_r_hand_letter_pairs()))
right_p = batch(typist(get_r_hand_pairs()))
vitamin_c = batch(typist(get_vitamin_c()))

# print the typing tests.
print("Left Hand")
print(left)
print("")
print("Right Hand")
print(right)
print("Right Hand With Punct.")
print(right_p)
print ("vitamin c")
print(vitamin_c)
