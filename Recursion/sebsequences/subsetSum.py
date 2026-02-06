from typing import *

class Solutioin:
    
    '''
    Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

    Examples

    Input: N = 3, arr[] = {5,2,1}
    Output: 0,1,2,3,5,6,7,8
    Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8

    Input: N=3,arr[]= {3,1,2}
    Output: 0,1,2,3,3,4,5,6
    Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6
    '''
    def subsetSum(self, idx: int, sum: int, arr: List[int], res: List[int]) -> List[int]:
        if idx == len(arr):
            res.append(sum)
            return
        
        self.subsetSum(idx + 1, sum + arr[idx], arr, res) 
        self.subsetSum(idx + 1, sum, arr, res) 
    
if __name__ == "__main__":
    arr = [5,2,1]
    res = []
    sols = Solutioin()
    sols.subsetSum(0, 0, arr, res)
    print("Output: ", sorted(res))
    
    arr = [3, 1, 2]
    res = []
    sols = Solutioin()
    sols.subsetSum(0, 0, arr, res)
    print("Output: ", sorted(res))
