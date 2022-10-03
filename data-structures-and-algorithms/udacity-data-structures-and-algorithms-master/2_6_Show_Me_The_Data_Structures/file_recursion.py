import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.Note that a path may 
    contain further subdirectories and those subdirectories may also contain
    further subdirectories.There are no limit to the depth of the subdirectories
    can be.

    Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system

    Returns:
        list: a list of paths
    """
    if os.path.isfile(path) and suffix in path:
        return [path]
    elif os.path.isdir(path):
        paths = []
        for dirs in os.listdir(path):
          files = find_files(suffix, os.path.join(path, dirs))
          if files is not None:
            paths += files
        return paths


if __name__ == '__main__':
    for path in find_files('.c', './testdir'):
        print(path)
