#Alexander Starr
#22C:016:A01
#00567613

from computeWordFrequencies import computeWordFrequencies
from mostFrequentWords import mostFrequentWords

def merge(words1, freq1, words2, freq2):
    # Merges two word lists, updating the frequencies.
    index = 0
    while index < len(words2):
        word = words2[index]
        # Walks through words2, checking to see if each word is in words1.
        # If a word is in words1, then it creates an index for where that word
        # appears in words1, then uses this to update the corresponding freq.
        # If the word does not appear in words1, then it appends it to words1,
        # and appends the corresponding frequency to freq1.
        if word in words1:
            alt_index = words1.index(word)
            freq1[alt_index] = freq1[alt_index] + freq2[index]
        else:
            words1.append(word)
            freq1.append(freq2[index])
        index = index + 1
    return [words1, freq1]

# Generates the lists of all words >= 4 letters and their frequencies.
tolstoy = computeWordFrequencies("war.txt")
stevenson = computeWordFrequencies("hyde.txt")
stevenson2 = computeWordFrequencies("treasure.txt")

# Combines the two Stevenson novels
stevenson = merge(stevenson[0],stevenson[1],stevenson2[0],stevenson2[1])

# Finds the top 20 most frequent words from the created lists.
tolstoy_top20 = mostFrequentWords(tolstoy[0], tolstoy[1], 20)
stevenson_top20 = mostFrequentWords(stevenson[0], stevenson[1], 20)

print "Tolstoy's Top 20 Most Common Words:"
print tolstoy_top20
print "Stevenson's Top 20 Most Common Words:"
print stevenson_top20