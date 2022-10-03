def min_platforms(arrival: int, departure:int) -> int:
    """
    Returns the minimum number of platforms required so that
    trains do not have to wait.

    Args:
        arrival (list): list of arrival times
        departure (list): list of departure times
    Returns:
        int: minimum number of platforms required
    """
    arrival = sorted(arrival)
    departure = sorted(departure)

    min_platforms = 1
    current_platform = 1
    arrival_count = 1
    departure_count = 0

    while arrival_count < len(arrival) and departure_count < len(departure):
        if arrival[arrival_count] < departure[departure_count]:
            current_platform += 1
            arrival_count += 1
        elif arrival[arrival_count] >= departure[departure_count]:
            current_platform -= 1
            if current_platform < 0:
                current_platform = 0
            departure_count += 1
        if current_platform > min_platforms:
            min_platforms = current_platform
    return min_platforms


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arrival = [900,  940, 950,  1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    test_case = [arrival, departure, 3]
    test_function(test_case)

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 340, 320, 430, 400, 520]
    test_case = [arrival, departure, 2]
    test_function(test_case)
