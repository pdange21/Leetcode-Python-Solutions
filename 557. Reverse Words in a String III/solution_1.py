class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(' ') #words contains words splitted by space

        return ' '.join(w[::-1] for w in words) #reversing the word and joining using space
        