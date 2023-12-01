class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0 #index of word
        i = j = 0 #index of char

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False
            
            i, j = i+1, j+1

            if i == len(word1[w1]):
                w1 += 1 #incrementing to the next word
                i = 0 #resetting the pointer
            if j == len(word2[w2]):
                w2 += 1 #incrementing the word to the next word
                j = 0 #resetting the pointer
            
        if w1 != len(word1) or w2 != len(word2): #one of the word is not ended
            return False
        
        return True # all the cases are passed
            
        