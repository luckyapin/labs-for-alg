def hash_sum(s, table_size):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
    return hash_value % table_size

class HashTable:
    def __init__(self, size):
        self.size = size #
        self.table = [[] for _ in range(self.size)]

    def add_value(self, key, value):
        hash_key = hash_sum(key, self.size)
        bucket = self.table[hash_key]
        for kv in bucket:
            if kv[0] == key:
                kv[1] = value
                return
        bucket.append([key, value])

    def get_value(self, key):
        hash_key = hash_sum(key, self.size)
        bucket = self.table[hash_key]
        for kv in bucket:
            if kv[0] == key:
                return kv[1]
        return None