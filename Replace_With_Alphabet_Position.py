'''In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.'''

def alphabet_position(text):
    list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    text2 = text.lower()
    a = []
    for x in range(len(text2)):
        if text2[x] in list:
            a.append(list.index(text2[x])+1)
        else:
            pass
    return(' '.join(map(str,a)))
