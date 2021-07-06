# class LinkedList:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    # def fnv1(self, key):
    """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        str_bytes = key.encode()

        hash_total = 5381

        for b in str_bytes:
            hash_total = ((hash_total << 5) + hash_total) + b
            hash_total &= 0xffffffff

        return hash_total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Find the hash index
        # Search the list for the key
        # If it's there, replace the value
        # If it's not, append a new record to the list

        index = self.hash_index(key)
        current = self.storage[index]

        if current is not None:
            # loop to search the list for the key
            while current is not None:
                if current.key == key:
                    # If it's there, replace the value
                    current.value = value
                    break

                current = current.next
            # If it's not there, append a new record to the list
            else:
                new_node = HashTableEntry(key, value)
                new_node.next = self.storage[index]
                self.storage[index] = new_node

        else:
            self.storage[index] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Find the hash index
        # Search the list for the key
        # If found, delete the node from the list, (return the node or value?)
        # Else return None

        # Find the hash index
        index = self.hash_index(key)

        # Search the list for the key
        if self.storage[index] is not None:
            # If found, delete the node from the list
            if self.storage[index].key == key:
                self.storage[index].value = None
            else:
                current = self.storage[index].next
                while current is not None:
                    if current.key == key:
                        current.value = None
                    current = current.next
        # Else return None
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # Find the hash index
        index = self.hash_index(key)

        # Search the list for the key
        if self.storage[index].key == key:
            # If found, return the value
            return self.storage[index].value

        else:
            current = self.storage[index].next
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        # Step 1: make a new, bigger table/array
        # Step 2: go through all the old elements, and hash into the new list

        # make a new, bigger table/array
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # go through all the old elements
        # hash into the new list
        for item in old_storage:

            if item is not None and item.next is None:
                self.put(item.key, item.value)
            if item is not None and item.next is not None:
                current = item
                while current.next is not None:
                    self.put(current.key, current.value)
                    current = current.next
                self.put(current.key, current.value)
        return


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
