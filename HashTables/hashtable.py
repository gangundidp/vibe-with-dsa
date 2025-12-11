BLANK = object()

#  The traditional hash table is backed by an array capable of storing only one data type.
class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]
    
    def __len__(self):
        return len(self.values)
    
    def __setitem__(self, key, value):
        # index = hash(key) % len(self)   # You turn an arbitrary key into a numeric hash value and use the modulo operator to constrain the resulting index within the available address space. 
        self.values[self._index(key)] = value
        # (venv) C:\> set PYTHONHASHSEED=128    disable hash randomization or use a predictable seed when running pytest
        # (venv) C:\> python -m pytest
    
    def __getitem__(self, key):
        # index = hash(key) % len(self)
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value
        
    def __contain__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
        
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __delitem__(self, key):
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)
        
    def _index(self, key):
        return hash(key) % len(self)
        
        
    