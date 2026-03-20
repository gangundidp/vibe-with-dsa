from typing import *

class Solution:
    def assignCookiesMemorization(self, students: List[int], cookies: List[int]):
        students.sort()
        cookies.sort()
        
        res = [[]] * len(students)
        count = 0
        
        i = 0
        j = 0
        
        while i < len(students) and j < len(cookies):
            if cookies[j] < students[i]:
                j += 1
                continue
            
            if cookies[j] >= students[i]:
                res[i] = cookies[j]
                count += 1
                i += 1
                j += 1
            
        return count
    
    def findContentChildren(self, student, cookie):
        student.sort()
        cookie.sort()

        # Recursive helper function with memoization
        def helper(studentIndex, cookieIndex):
            # Base case: if we reach end of either list
            if studentIndex >= len(student) or cookieIndex >= len(cookie):
                return 0

            result = 0

            # If the cookie satisfies the student's greed
            if cookie[cookieIndex] >= student[studentIndex]:
                # Option 1: assign this cookie and move to next student and cookie
                result = max(result, 1 + helper(studentIndex + 1, cookieIndex + 1))

            # Option 2: skip this cookie and try the next one for the same student
            result = max(result, helper(studentIndex, cookieIndex + 1))

            return result

        # Start recursion from index 0 for both arrays
        return helper(0, 0)

    
if __name__ == "__main__":
    sols = Solution()
    students = [1, 2, 3]
    cookies = [1, 1]
    print("Output: ", sols.assignCookiesMemorization(students, cookies))
    print("Output: ", sols.findContentChildren(students, cookies))
    
    students = [1, 2]
    cookies = [1, 2, 3]
    print("Output: ", sols.assignCookiesMemorization(students, cookies))
    print("Output: ", sols.findContentChildren(students, cookies))