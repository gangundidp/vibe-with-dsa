import array as arr

# a=arr.array(data type,value list)  
arr1 = arr.array('d', [1.0, 2.0, 3.0])
print(arr1)

print('Length of Array: ', arr1)

arr1.append(3.3)
print(arr1)

arr1.extend([4.3, 65.4])
print(arr1)

popped_element = arr1.pop(3) # takes index as parameter and returns element
print('Popped Element: ', popped_element, ' arr1: ', arr1) 

Removed_element = arr1.remove(2.0) # takes element as parameter and returns nothing (None).
print(f'Removed Element: {Removed_element} and Arr1: {arr1}' )

arr2 = arr.array('d', [4, 9.3])
print('arr1 + arr2: ', arr1 + arr2)

for ele in arr1:
    print(ele, end=' ')


