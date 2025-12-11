from array import array as arr
def isArraySorted(arr):
    isSorted = False
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            isSorted = True
        if isSorted == False:
            return isSorted
    return isSorted

if __name__ == "__main__":
    arr = arr('i', [1, 2, 3, 3, 5])
    print("Is Array sorted: ", isArraySorted(arr))