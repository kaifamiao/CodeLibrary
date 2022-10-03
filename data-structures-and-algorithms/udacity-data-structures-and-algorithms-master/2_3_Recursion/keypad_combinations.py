def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def possible_strings(num: int) -> list:
    """
    Returns all the possible strings that can be written using the given
    keypad digits.
    """
    if num == 0:
        return ['']
    elif num / 10 < 1:
        return [char for char in get_characters(num)]
    else:
        result = []
        
        chars = get_characters(num % 10)
        previous = possible_strings(num // 10)

        for char in chars:
            for prev in previous:
                result.append(prev + char)
        return result


def test_keypad(input, expected_output):
    if sorted(possible_strings(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


if __name__ == '__main__':
    input = 0
    expected_output = [""]
    test_keypad(input, expected_output)

    input = 23
    expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    test_keypad(input, expected_output)

    input = 32
    expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
    test_keypad(input, expected_output)

    input = 8
    expected_output = sorted(["t", "u", "v"])
    test_keypad(input, expected_output)

    input = 354
    expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
    test_keypad(input, expected_output)
