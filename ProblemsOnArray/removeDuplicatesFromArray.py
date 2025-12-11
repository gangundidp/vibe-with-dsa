from array import array as arr
def removeDuplicates(arr):
    temp = []
    for ele in arr:
        if len(temp) == 0:
            temp.append(ele)
        if (temp[-1] != ele):
            temp.append(ele)
        
    return temp

def removeDuplicatesOptimal(arr):
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    return arr[:i+1]

if __name__ == "__main__":
    arr = arr('i', [1, 33, 33, 44, 88, 88, 88, 100, 100, 100, 1000, 2343])
    print('Array after removing duplicates: ', removeDuplicates(arr))
    print('Array after removing duplicates: ', removeDuplicatesOptimal(arr))