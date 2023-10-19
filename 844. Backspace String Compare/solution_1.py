class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspace(s: str) -> str:
            '''function which handles the string operation which contain #'''
            stack = [] #empty stack
            for c in s: #iterate through the string
                if c != '#': #if do not encounter this we add to the stack 
                    stack.append(c)
                elif stack: #if we encounter '#' and the stack is not empty we pop from the stack
                    stack.pop()
            return stack #return the stack
        
        return backspace(s) == backspace(t) #compare the two string
        