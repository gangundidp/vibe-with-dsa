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
        

if __name__ == "__main__":
    sols = Solution()
    s = 'tree'
    print("Output: ", sols.sortCharactersByFrequency(s))