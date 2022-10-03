def reverse_string(string: str) -> str:
    """Returns the reverse of the given string."""
    if len(string) <= 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


if __name__ == '__main__':
    print ("Pass" if  ("" == reverse_string("")) else "Fail")
    print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
