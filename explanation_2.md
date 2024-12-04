## Problem 2: File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## Reasoning Behind Decisions:

The problem can be solved using a recursive approach. The function will take a directory path as input and recursively traverse the directory structure to find all files that end with for example ".c". If a directory is encountered during the traversal, the function will recursively call itself on that directory to find all files within that directory.

The function will use the `os` module in Python to interact with the file system and traverse the directory structure. The `os.listdir()` function can be used to get a list of all files and directories in a given directory. The `os.path.join()` function can be used to construct the full path of a file or directory by joining the directory path with the file or directory name.

The function will return a list of all files that end with a given file extension in the directory and its subdirectories.


## Time Efficiency:

The time complexity of the function will depend on the number of files and directories in the directory structure. The function will traverse the directory structure recursively, visiting each file and directory once. The time complexity of the function will be O(n), where n is the total number of files and directories in the directory structure.



## Space Efficiency:

The space complexity of the function will depend on the number of files and directories in the directory structure. The space complexity of the function will be O(n), where n is the total number of files and directories in the directory structure.
