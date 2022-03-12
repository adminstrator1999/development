class HashTable:

    # create empty bucket lis of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_value(self, key, value):

        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size

        # Get the bucked corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            # check if the bucked has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
        # If the bucket has the same key as the key to be inserted,
        # update the key value
        # Otherwise append the new key-value pair to thee bucked
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append([key, value])

    # Return searched value with specific key
    def get_value(self, key):

        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break
        if found_key:
             return record_value
        else:
            return "No record found"

    def delete_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


