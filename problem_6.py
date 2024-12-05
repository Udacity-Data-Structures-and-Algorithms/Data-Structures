from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    set_union = set()

    # Add all elements from the first linked list to the set
    node = llist_1.head
    while node:
        set_union.add(node.value)
        node = node.next

    # Add all elements from the second linked list to the set
    node = llist_2.head
    while node:
        set_union.add(node.value)
        node = node.next


    # Create a new linked list to store the union
    union_llist = LinkedList()
    for value in set_union:
        union_llist.append(value)

    return union_llist

    

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    set_1 = set()

    # Add all elements from the first linked list to the set
    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next

    # Add all elements from the second linked list to the set
    set_2 = set()
    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next

    

    # Find the intersection of both sets
    set_intersection = set_1.intersection(set_2)


    # Create a new linked list to store the intersection
    intersection_llist = LinkedList()
    for value in set_intersection:
        intersection_llist.append(value)

    return intersection_llist

def linked_list_to_set(llist: LinkedList) -> set:
    """Helper function to convert LinkedList to set for comparison"""
    result = set()
    current = llist.head
    while current:
        result.add(current.value)
        current = current.next
    return result

if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    # Test union
    union_result = union(linked_list_1, linked_list_2)
    expected_union = {1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65}
    assert linked_list_to_set(union_result) == expected_union

    # Test intersection
    intersection_result = intersection(linked_list_1, linked_list_2)
    expected_intersection = {4, 6, 21}
    assert linked_list_to_set(intersection_result) == expected_intersection

    # Test case 2 - identical lists
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]

    for i in element_1:
        linked_list_5.append(i)
    for i in element_2:
        linked_list_6.append(i)

    # Test union with identical lists
    union_result = union(linked_list_5, linked_list_6)
    expected_union = {2, 3, 4, 6, 21, 35, 65}
    assert linked_list_to_set(union_result) == expected_union

    # Test intersection with identical lists
    intersection_result = intersection(linked_list_5, linked_list_6)
    expected_intersection = {2, 3, 4, 6, 21, 35, 65}
    assert linked_list_to_set(intersection_result) == expected_intersection

    # Test case 3 - one empty list
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = []

    for i in element_1:
        linked_list_7.append(i)
    for i in element_2:
        linked_list_8.append(i)

    # Test union with empty list
    union_result = union(linked_list_7, linked_list_8)
    expected_union = {2, 3, 4, 6, 21, 35, 65}
    assert linked_list_to_set(union_result) == expected_union

    # Test intersection with empty list
    intersection_result = intersection(linked_list_7, linked_list_8)
    expected_intersection = set()
    assert linked_list_to_set(intersection_result) == expected_intersection

    print("All test cases passed!")

