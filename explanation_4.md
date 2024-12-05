
## Problem 4: Active Directory

### Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

## Reasoning Behind Decisions:

Implemented a recursive approach to solve this problem because it allows me to search through the groups and users in the Active Directory in a more efficient way. By using a recursive function, I can search through each group and user in the Active Directory until I find the user I am looking for. 

## Time Complexity:
    ---------------
    O(N), where N is the total number of groups and users in the group hierarchy.
    The algorithm needs to potentially visit every group and check its users list
    in the worst case scenario where the user is not found or is in the last group checked.

## Space Complexity:
    ----------------
    O(M), where M is the maximum number of groups that need to be stored in the stack
    at any point. In the worst case, this could be equal to the total number of groups
    if the group structure is linear (each group having one subgroup).



