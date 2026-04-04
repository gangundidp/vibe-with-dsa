class Solution:
    def maxMeetings(self, start, end):
        meetings = [(end[i], start[i], i + 1) for i in range(len(start))]
        meetings.sort()

        result = []
        last_end = -1

        for e, s, idx in meetings:
            if s > last_end:  
                result.append(idx)  
                last_end = e  
        return result


if __name__ == "__main__":
    sol = Solution()
    start = [1, 3, 0, 5, 8, 5]
    end   = [2, 4, 6, 7, 9, 9]

    print("Output: ", sol.maxMeetings(start, end))
