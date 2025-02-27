## FIRST IMPLEMENTATION
def invert_string(string):
    inverted = ""
    word = ""
    for i in range(len(string)):
        if string[i] != " ":
            word = word + string[i]

        if string[i] == " " or i == len(string)-1:
            new_word = ""
            for i in range(len(word)-1, -1, -1):
                new_word = new_word + word[i]
            if i != len(string) - 1:
                inverted = inverted + new_word + " "
            else: 
                inverted = inverted + new_word
            word = ""
    return inverted
