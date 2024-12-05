
## Problem 4: Active Directory

### Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

## Reasoning Behind Decisions:

Implemented a recursive approach to solve this problem because it allows me to search through the groups and users in the Active Directory in a more efficient way. By using a recursive function, I can search through each group and user in the Active Directory until I find the user I am looking for. 


## Time Efficiency:

The time complexity of this function is O(n) where n is the number of groups and users in the Active Directory. This is because the function must search through each group and user in the Active Directory to find the user. In the worst case, the function will have to search through all the groups and users in the Active Directory to find the user.


## Space Efficiency:

The space complexity of this function is O(n) where n is the number of groups and users in the Active Directory. This is because the function must store the groups and users in the Active Directory in a data structure to search through them. In the worst case, the function will have to store all the groups and users in the Active Directory in the data structure to search through them.



