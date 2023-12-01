class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        #naive and brute force approach requires extra O(n) memory
        string_word1 = string_word2 = ""

        for i in word1:
            string_word1 += i
        
        for j in word2:
            string_word2 += j
        
        if string_word1 == string_word2:
            return True
        return False