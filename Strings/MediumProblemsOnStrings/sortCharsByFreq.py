class Solution:
    '''
    Problem Statement: You are given a string s. Return the array of unique characters, sorted by highest 
    to lowest occurring characters. If two or more characters have same frequency then arrange them in 
    alphabetic order.

    Example 1:
    Input:
    s = "tree"
    Output:
    ['e', 'r', 't']
    Explanation:

    e → 2
    r → 1
    t → 1
    Since 'r' and 't' have the same frequency, they are sorted alphabetically → 'r' comes before 't'.

    Example 2:
    Input:
    s = "raaaajj"
    Output:
    ['a', 'j', 'r']
    Explanation:

    a → 4
    j → 2
    r → 1
    Characters are sorted by decreasing frequency. In case of ties, alphabetically.
    '''
    def sortCharactersByFrequency(self, s):
        temp = []
        for i in range(26):
            temp.append((0, chr(i + ord('a'))))
        # print(temp)
        
        for ch in s:
            index = ord(ch) - ord('a')
            temp[index] = (temp[index][0] + 1,ch)
            
        temp.sort(key=lambda x: (-x[0], x[1]))
        # print(temp)
        result = [ch for i, ch in temp if i > 0]
        return result
        

if __name__ == "__main__":
    sols = Solution()
    s = 'tree'
    print("Output: ", sols.sortCharactersByFrequency(s))
    s = "raaaajj"
    print("Output: ", sols.sortCharactersByFrequency(s))