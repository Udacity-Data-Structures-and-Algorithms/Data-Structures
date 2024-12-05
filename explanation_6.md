
## Problem 6: Union and Intersection


## Union Function

### Reasoning Behind Decisions:

The union function uses a set to store the values of the linked lists. The union function then iterates through the linked lists and adds the values to the set. The union function then creates a new linked list and adds the values from the set to the new linked list. The union function then returns the new linked list. This approach ensures that the union of the two linked lists is computed efficiently and without duplicates. 



### Time Efficiency:

    Time Complexity:
    --------------
    O(n + m) where n and m are the lengths of the input linked lists
    - Converting lists to sets: O(n) + O(m)
    - Set operations: O(1) average case
    - Creating result list: O(k) where k <= n + m

### Space Efficiency:

    Space Complexity:
    ---------------
    O(n + m) where n and m are the lengths of the input linked lists
    - Set storage: O(n) + O(m) in worst case
    - Result linked list: O(n + m) in worst case

## Intersection Function

### Reasoning Behind Decisions:

The intersection function uses a set to store the values of the first linked list. The intersection function then iterates through the second linked list and checks if the value is in the set. If the value is in the set, the intersection function adds the value to a new linked list. The intersection function then returns the new linked list.

### Time Efficiency:

    Time Complexity:
    --------------
    O(n + m) where n and m are the lengths of the input linked lists
    - Converting lists to sets: O(n) + O(m)
    - Set intersection: O(min(n,m))
    - Creating result list: O(k) where k <= min(n,m)

### Space Efficiency:

    Space Complexity:
    ---------------
    O(n) where n is the length of the first linked list
    - Two set storage: O(n) + O(m) in worst case
    - Result linked list: O(min(n,m)) in worst case

