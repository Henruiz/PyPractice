class HashTable:

    def __init__(self, size):
        self.size = size  # setting size of the array
        self.map = [None] * self.size  # array where we are storing to with fixed len

    def _get_hash(self, key):
        local_hash = 0
        for char in str(key):
            local_hash += ord(char)
        return local_hash % self.size  # returns index

    def add(self, key, value):
        key_hash = self._get_hash(key)  # index value to place it in
        key_value = [key, value]  # what we want to insert

        if self.map[key_hash] is None:  # if empty add
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)  # if it a new key append to the list
            return True

    def get(self, key):
        # get the hash given the key and if the cell is not empty just grab else return none
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        # locate key, check if the cell is empty, return false if empty else iterate through the has and
        # when found remove
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('-------Testing-------')
        for item in (self.map):
            if item is not None:
                print(str(item))


#  trying to figure out how to display it as a single array/list
# def get_keys(self):
#     keys = []
#     for i in len(self.map):


ht = HashTable(50)
ht.add("A", "0")
ht.add("B", "1")
ht.add("C", "2")
ht.add("D", "3")
ht.add("E", "4")
ht.add("F", "5")
ht.add("G", "6")
ht.add("H", "7")
ht.add("I", "8")
ht.add("J", "9")
ht.print()
ht.delete("J")
ht.print()
x = ht.get("H")
print(x)