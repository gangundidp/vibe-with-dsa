def merge_sort(lst, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(lst, low, mid)
    merge_sort(lst, mid+1, high)
    merge(lst, low, mid, high)
    return lst

def merge(lst, low, mid, high):
    left, right, temp = low, mid+1, []
    
    while (left <= mid) and (right <= high):
        if lst[left] <= lst[right]:
            temp.append(lst[left])
            left += 1
        else:
            temp.append(lst[right])
            right += 1
    
    while (left <= mid):
        temp.append(lst[left])
        left += 1
    
    while (right <= high):
        temp.append(lst[right])
        right += 1
        
    for i in range(len(temp)):
        lst[low + i] = temp[i]

if __name__ == "__main__":
    lst = [39, 903, -49, 0, 3]
    print(merge_sort(lst, 0, len(lst)-1))