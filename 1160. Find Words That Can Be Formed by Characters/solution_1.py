class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count_chars = Counter(chars) #hashmap for chars
        res = 0

        for w in words: #w is the word
            cur_word = defaultdict(int)
            flag = True
            for c in w: #c is the character
                cur_word[c] += 1
                if c not in count_chars or cur_word[c] > count_chars[c]:
                    flag = False
                    break #Break out of the loop as there is no point of iterating through the word
            if flag:
                res += len(w) #if the flag is true then we add the length
        return res