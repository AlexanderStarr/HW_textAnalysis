#Alexander Starr
#22C:016:A01
#00567613

from parse import parse

def computeWordFrequencies(filename):
    # Takes a string called 'filename' and reads from a file of that name.
    # Returns a list 'L', consisting of two lists.
    # L[0] is the list of all distinct, lowercase words of length at least 4.
    # L[1] is the list of corresponding frequencies of these words.
    f = open(filename, "r")
    distinct_words = []
    occurrences = []
    line = f.readline()
    while line:
        # While 'line' is non-empty, the line is first parsed into a list.
        # Then each word in the list is checked against 'distinct_words'
        # If the word is not in 'distinct_words', then it is added and...
        # the number of occurrences for that word is set to 1.
        # Note that the index of each word is the same as the index of...
        # its corresponding number of occurrences.
        words_in_line = parse(line)
        #print words_in_line     #Debugging print statement.
        index = 0
        while index < len(words_in_line):
            word = words_in_line[index]
            if word not in distinct_words:
                distinct_words.append(word)
                occurrences.append(1)
                # If the word is not unique, then the index for that word...
                # is used to add 1 to the number of occurrences with the
                # corresponding index.
            else:
                word_index = distinct_words.index(word)
                occurrences[word_index] = occurrences[word_index] + 1
            index = index + 1
        line = f.readline()
    f.close()
    L = [distinct_words, occurrences]
    return L

# The below code was used to test a file with a known number of occurrences.
#L = computeWordFrequencies("test.txt")
#for index in range(0, len(L[0])):
#    print L[0][index], "-", L[1][index]