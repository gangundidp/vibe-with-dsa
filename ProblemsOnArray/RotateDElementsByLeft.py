from array import array as arr
def rotateDElementsByLeft(arr, d):
    temp = []
    for i in range(d):
        temp.append(arr[i])
        
    i = 0
    for j in range(d, len(arr)):
        arr[i] = arr[j]
        i += 1
    
    for k in range(len(temp)):
        arr[i] = temp[k]
        i += 1
    return arr


if __name__ == "__main__":
    arr = arr('i', [3, 9, 0, 7, 4])
    print('Rotated by one left: ', rotateDElementsByLeft(arr, 2))