from typing import List

class Solution:
    def medianTwoSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]
        
    def medianTwoSortedArrayUsingMergeSort(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge(nums1, nums2)
        n = len(merged)

        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i = j = 0
        merged_list = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1

        merged_list.extend(left[i:])
        merged_list.extend(right[j:])
        return merged_list

        
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.medianTwoSortedArrays(nums1, nums2))  # Output: 2.0