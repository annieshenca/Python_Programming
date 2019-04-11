# Create and design a hashmap in Python
# Annie Shen

class Hashmap:
    # Init variables essential to each hashmap
    def __init__(self):
        self.size = 64 # A arbitory length
        self.map = [None] * self.size # A list with fixed length
    
    # To prevent collisions and minimum amount of key-value per index,
    # let the hash value be determined by the sum of ASCII values of 
    # each letter in key. Mod the value
    def _get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        # Perform the _get_hash function to know which cell to store key-value in the hashmap.
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        # Check if that cell in map is empty.
        if self.map[k] is None:
            self.map[hashed_key] = list([key_value])
            return True
        
        # Else, the cell is already taken by some other key.
        # Check if the key already exists in the cell, if so, update the value.
        # If not, the append the key-value to the list.
        else:
            for pairs in self.map[key_hash]:
                if pair[0] == key:
                    # Update the value, since the key already exists
                    pair[1] = value
                    return True
                else:
                    # Append the new key-value pair
                    self.map[key_hash].append(key_value)
            return True
    
    # Given a key, check if the hashmap storage has the given key. If yes, return
    # the value of the key. If not, return None.
    def get(self, key):
        key_hash = self._get_hash(key)
        # Check if the key exists in our map
        if self.map[key_hash] is not None:
            for pairs in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    # Find and delete the given key from hashmap. If the key does not exist in the
    # hashmap, then return None.
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            # Using for-loop here because we need to get the specific index.
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    # Delete by pop
                    self.map[key_hash].pop(i)
                    return True

        # The key that needs deletion does not exist in hashmap.
        return False
    

    # Print helper function
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))


# Driver code
h = Hashmap()
h.add('1', 'one')
h.add('2', 'two')
h.add('3', 'three')
h.add('3', 'three and a half')

h.print()
h.delete('3')
h.print()
print("2: " + h.get('2'))


