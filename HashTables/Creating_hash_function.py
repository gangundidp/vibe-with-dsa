import sys
print(sys.hash_info.algorithm)   # gives which hash algorithm python interpreter using.py 

# def hash_function(key):
#     return sum(ord(char) for char in key)

# def hash_function(key):
#     return sum(ord(char) for char in str(key))  # converting into string makes hash function available to all types

# def hash_function(key):
#     return sum(ord(char) for char in repr(key))  # converting into string makes hash function available to all types

def hash_function(key):
    return sum(index * ord(char) for index, char in enumerate(repr(key).lstrip("'"), start=1))  # To tackle the issue with anagrams, like Loren and Loner

print(hash_function('lorem'))
print(hash_function('loren'))
print(hash_function('loner'))
print(hash_function(3.134))
print(hash_function(True))
print(hash_function('3.14'))
print(hash_function(3.14))
print(hash_function('this is hash function' * 1_000_000))