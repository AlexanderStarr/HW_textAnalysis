#Alexander Starr
#22C:016:A01
#00567613

def parse(s):
    # Returns a list containing all the words in s at least 4 letters long.
    # parsed_string and word are initialized to be empty,
    # they will be built as characters are scanned.
    parsed_string = []
    word = ""
    s = s.lower()
    index = 0
    # building_word keeps track of if a word is being built or not.
    # If False, the program scans characters for letters.
    # If True, then letters are added to the current word,
    # and the next non-letter character signifies the end of the word.
    building_word = False
    while index < len(s):
        if s[index] <= "z" and s[index] >= "a":
            building_word = True
            word = word + s[index]
        else:
            # The else block runs if a non-letter character is found.
            if building_word == True:
                # If we were building a word, the length is checked.
                # If long enough, then the word is added to the list.
                # Long enough or not, 'word' and 'building_word' are reset.
                if len(word) >= 4:
                    parsed_string.append(word)
                building_word = False
                word = ""
        index = index + 1
    if building_word:
        parsed_string.append(word)
    return parsed_string

# The below print statement is to test the above function.
# Note that words of 4 characters and greater make the list.
# Also note that repeated words ("united", "states") get stored each time.

# print parse("We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.")