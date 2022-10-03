def is_palindrome(string):
    """Checks whether the given string is palindrome or not."""
    if len(string) <= 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        return (string[0] == string[len(string) - 1]) & is_palindrome(string[1:-1])


if __name__ == '__main__':
    print ("Pass" if  (is_palindrome("")) else "Fail")
    print ("Pass" if  (is_palindrome("a")) else "Fail")
    print ("Pass" if  (is_palindrome("madam")) else "Fail")
    print ("Pass" if  (is_palindrome("abba")) else "Fail")
    print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
