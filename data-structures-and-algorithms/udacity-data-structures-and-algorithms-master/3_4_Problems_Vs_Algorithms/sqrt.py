import math


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    if number <= 1:
        return number
    
    left = 0
    right = math.floor(number / 2)
    while left <= right:
        mid = math.floor((left + right) / 2)
        i = mid * mid

        if i == number:
            return mid
        elif i < number:
            left = mid + 1
            approx = mid
        else:
            right = mid - 1
    return approx


if __name__ == '__main__':
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")