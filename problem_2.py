import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    # Initialize a list to store the file paths
    file_paths = []

    # Check if the path exists
    if not os.path.exists(path):
        return file_paths

    # Iterate over the files and directories in the given path
    for file in os.listdir(path):
        # Create the full path of the file
        full_path = os.path.join(path, file)

        # Check if the full path is a file
        if os.path.isfile(full_path):
            # Check if the file ends with the given suffix
            if full_path.endswith(suffix):
                file_paths.append(os.path.normpath(full_path))
        # Check if the full path is a directory
        elif os.path.isdir(full_path):
            # Recursively call the function to search for files in the subdirectory
            file_paths.extend(find_files(suffix, full_path))

    return file_paths


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    result = find_files(".c", "./testdir")
    assert result == [os.path.normpath('./testdir/subdir1/a.c'), os.path.normpath('./testdir/subdir3/subsubdir1/b.c'), os.path.normpath('./testdir/subdir5/a.c'), os.path.normpath('./testdir/t1.c')], f"Test Case 1 Failed: {result}"

    # Test Case 2
    result = find_files(".h", "./testdir")
    assert result == [os.path.normpath('./testdir/subdir1/a.h'), os.path.normpath('./testdir/subdir3/subsubdir1/b.h'), os.path.normpath('./testdir/subdir5/a.h'), os.path.normpath('./testdir/t1.h')], f"Test Case 2 Failed: {result}"

    # Test Case 3
    result = find_files(".gitkeep", "./testdir")
    assert result == [os.path.normpath('./testdir/subdir2/.gitkeep'), os.path.normpath('./testdir/subdir4/.gitkeep')], f"Test Case 3 Failed: {result}"

    # Test Case 4: Edge case with empty directory
    result = find_files(".c", "./testdir/subdir2")
    assert result == [], f"Test Case 4 Failed: {result}"

    # Test Case 5: Edge case with non-existent root directory
    result = find_files(".c", "./non_existent_dir")
    assert result == [], f"Test Case 5 Failed: {result}"

    print("All test cases passed!")
