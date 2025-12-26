class Solution:
    def isomorphic(self, s, t):
        n, m = [0] * 256 , [0] * 256

        length = len(s)

        for i in range(length):
            if n[ord(s[i])] != m[ord(t[i])]:
                return False
            
            n[ord(s[i])] = i + 1
            m[ord(t[i])] = i + 1
            
        return True
    
if __name__ == "__main__":
    sols = Solution()
    s = 'paper'
    t = 'title'
    print('Output: ', sols.isomorphic(s, t))
    s = 'foo'
    t = 'bor'
    print('Output: ', sols.isomorphic(s, t))