# Hash function
def hash_function(key, size):
    return key % size

# Insert using linear probing
def insert_linear(table, key):
    index = hash_function(key, len(table))
    while table[index] is not None:
        index = (index + 1) % len(table)
    table[index] = key

# Example usage
if __name__ == "__main__":
    # Hash table
    table_size = 5
    hash_table = [None] * table_size

    keys = [12, 7, 22, 17]

    for key in keys:
        insert_linear(hash_table, key)

    print("Hash Table (Linear Probing):")
    for i in range(table_size):
        print(f"Index {i}: {hash_table[i]}")


