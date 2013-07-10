#Alexander Starr
#22C:016:A01
#00567613

def mostFrequentWords(wordList, frequencyList, k):
    # Takes a list of strings, list of corresponding frequencies, and a number.
    # Returns a list of the top k most frequent words.
    # Ties are broken by which word appears first in 'wordList'.
    # NOTE: Will return odd results if k > (len(wordList) - 1)
    most_frequent_words = []
    counter = 0
    while counter < k:
        # Finds the index of the highest value in 'frequencyList'
        i = frequencyList.index(max(frequencyList))
        # Appends the corresponding word from 'wordList'
        most_frequent_words.append(wordList[i])
        # Since 'frequencyList' is temporary under this function,
        # we will just set the highest value to zero.
        # This will then make the next highest value now the highest.
        frequencyList[i] = 0
        counter = counter + 1
    return most_frequent_words

# The below code was used for testing
#words = ["alpha","charlie","delta","bravo","hotel","golf","foxtrot","echo"]
#frequencies = [10, 9, 8, 10, 1, 3, 5, 6]
#print mostFrequentWords(words, frequencies, 8)