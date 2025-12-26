from typing import *

class Solution:
    def reverseSentence(self, s: str):
        wordsList = []
        word = ''
        
        for char in s:
            if char != ' ':
                word += char
            # non-empty word
            elif word:
                wordsList.append(word)
                word = ''
                
        if word:
            wordsList.append(word)

        wordsList.reverse()
        result = ' '.join(wordsList)
        
        return result
    
    def reverseSentenceMethod2(self, s: str):
        length = len(s) - 1
        result = ''
        # word = ''
        
        while length >= 0:
            while length >= 0 and s[length] == ' ':
                length -=1

            if length < 0:
                break
            
            end = length
            
            while length >= 0 and s[length] != ' ':
                length -= 1
                
            word = s[length + 1:end+1]

            if result != ' ':
                result += ' '
                
            result += word
        return result
            
    
if __name__ == "__main__":
    sols = Solution()
    s = 'Welcome to the Programming'
    print("OUtput: ", sols.reverseSentence(s))
    print("OUtput: ", sols.reverseSentenceMethod2(s))
    # print("OUtput: ", sols.usingMethod(s))
                
        