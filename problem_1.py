from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key not in self.cache:
            return -1
        else:
            # Move the key to the end to mark it as the most recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if self.capacity == 0:
            return
        if key in self.cache:
            # Move the key to the end to mark it as the most recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity and self.capacity > 0:
            # Evict the least recently used item
            self.cache.popitem(last=False)
        self.cache[key] = value



if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2 : Edge case
    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    assert our_cache.get(1) == -1  # Returns -1, cache capacity is 0

    # Test Case 3 : Large capacity
    our_cache = LRU_Cache(1000)
    for i in range(1000):
        our_cache.set(i, i)

    for i in range(1000):
        assert our_cache.get(i) == i

    print("All test cases pass")


