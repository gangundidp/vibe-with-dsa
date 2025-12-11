class Array:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array += [element]

    def pop(self, index):
        return self.array.pop(index)
    
    def length(self):
        len = 0
        for ele in self.array:
            len += 1

        return len
    
arr = Array()
arr.array = [1,2,3]
print(arr.array)
print(arr.pop(2))
print(arr.length())
arr.push(4)
print(arr.array)
