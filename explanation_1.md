
## Problem: LRU (Least Recently Used) Cache

Implement an LRU (Least Recently Used) cache. An LRU cache is a cache that has a maximum capacity. When the cache is full, the least recently used item is removed to make room for the new item. The cache should support the following operations:

- `get(key)`: Get the value of the key if the key exists in the cache, otherwise return -1.
- `put(key, value)`: Set or insert the value if the key is not already present. When the cache reaches its maximum capacity, it should invalidate the least recently used item before inserting a new item.



## Reasoning Behind Decisions:

The LRU cache is implemented using OrderdDict from collections module. OrderedDict is a dictionary subclass that maintains the order in which keys were inserted. This allows us to keep track of the least recently used item and remove it when the cache reaches its maximum capacity. The OrderedDict provides O(1) time complexity for get and set operations, making it an efficient choice for implementing the LRU cache.



## Time Efficiency:

The time complexity of the `get` operation is O(1) since it involves a single lookup in the dictionary. The time complexity of the `set` operation is also O(1) since it involves inserting or updating a key-value pair in the dictionary. The OrderedDict data structure provides O(1) time complexity for both get and put operations, making it an efficient choice for implementing the LRU cache.



## Space Efficiency:

The space complexity of the LRU cache is O(capacity) since it stores a maximum of `capacity` key-value pairs in the cache. The space complexity of the OrderedDict data structure is also O(capacity) since it stores the key-value pairs in the order of insertion. Overall, the space complexity of the LRU cache is O(capacity).

