def bubble_sort(lst):
    sort = 1
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                sort = 0
        if sort == 1: # sorted list, break the loop
            break
            
    return lst

if __name__ == "__main__":
    lst = [93, 9, -2, 85, 0]
    print(bubble_sort(lst))