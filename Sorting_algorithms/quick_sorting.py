def quick_sort(lst, low, high):
    if low < high:
        pv_pos = partition(lst, low, high)
        quick_sort(lst, low, pv_pos)
        quick_sort(lst, pv_pos + 1, high)
        return lst
    
def partition(lst, low, high):
    i, j, pivot = low-1, low, lst[high]

    while j<high:
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        elif lst[j] > pivot:
            j += 1
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i

if __name__ == "__main__":
    lst = [39, 3, 903, -49, 0, 3]
    print(quick_sort(lst, 0, len(lst)-1))

    
    