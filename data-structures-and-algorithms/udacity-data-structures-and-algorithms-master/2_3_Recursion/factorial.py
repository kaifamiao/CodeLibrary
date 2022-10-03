def factorial(n: int) -> int:
    """Returns n!"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print ("Pass" if (1 == factorial(0)) else "Fail")
    print ("Pass" if  (1 == factorial(1)) else "Fail")
    print ("Pass" if  (120 == factorial(5)) else "Fail")