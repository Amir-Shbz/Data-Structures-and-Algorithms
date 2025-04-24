# A sentence is a list of words that are separated by a single space with no 
# leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each 
# word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

class Solution:
    def sortSentence(self, s: str) -> str:
        sent = s.split()

        # sent.sort(key= lambda x : x[-1])

        for i in range(0, len(sent)-1):
            key = i
            for j in range(i+1, len(sent)):
                if int(sent[key][-1]) > int(sent[j][-1]):
                    key = j

            value = sent[key]
            sent[key] = sent[i]
            sent[i] = value

        for i in range(0, len(sent)):
            sent[i] = sent[i][0:-1]

        return ' '.join(sent)    
