import string

# DIGITS = "0123456789"
# LOWER_CASE = "qwertyuiopasdfghjklzxcvbnm"
# UPPER_CASE = "QWERTYUIOPASDFGHJKLZXCVBNM"


def cheak_password(password):
    if not isinstance(password, str) or len(password.strip()) == 0:
        return -1

    password = password.strip()
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    if len(password) < 8:
        return "too weak"

    #is_digit = True
    if (all(ch in digit for ch in password)
        or all(ch in lower for ch in password)
        or all(ch in upper for ch in password)):
    # for ch in password:
    #     if ch not in DIGITS:
    #         is_digit = False
    #         break
    #
    # is_lower = True
    #
    # for ch in password:
    #     if ch not in LOWER_CASE:
    #         is_lower = False
    #         break
    #
    # is_upper = True
    #
    # for ch in password:
    #     if ch not in UPPER_CASE:
    #         is_lower = False
    #         break
    #
    # if is_upper or is_lower or is_digit:
        return "weak"



    #is_digit = True
    if (any(ch in digit for ch in password)
        and any(ch in lower for ch in password)
        and any(ch in upper for ch in password)):

    # is_digit = False
    # for ch in password:
    #     if ch in DIGITS:
    #         is_digit = True
    #         break
    #
    # is_lower = False
    # for ch in password:
    #     if ch in UPPER_CASE:
    #         is_upper = True
    #         break
    # if is_upper and is_lower and is_digit:
        return "very strong"

    return "strong"


if __name__ == '__main__':
    assert cheak_password("") == -1
    assert cheak_password(" ") == -1
    #assert cheak_password("%$&#) == -1
    assert cheak_password(None) == -1
    assert cheak_password(10) == -1
    assert cheak_password(10.5) == -1
    assert cheak_password([1, 2, 3, 4, 5, 6]) == -1

    assert cheak_password("qwertyu") == "too weak"
    assert cheak_password("1234567") == "too weak"
    assert cheak_password("QWERTYU") == "too weak"
    assert cheak_password("QW12345") == "too weak"

    assert cheak_password("12345678") == "weak"
    assert cheak_password("123456789") == "weak"
    assert cheak_password("QWERTYUI") == "weak"
    assert cheak_password("QWERTYUIO") == "weak"
    assert cheak_password("qwertyui") == "weak"
    assert cheak_password("qwertyuio") == "weak"

    assert cheak_password("1234QWER") == "strong"
    assert cheak_password("12345678QWERRTT") == "strong"
    assert cheak_password("QWERyuik") == "strong"
    assert cheak_password("qwrety123456") == "strong"
    assert cheak_password("qwer1234") == "strong"

    assert cheak_password("123qweFG") == "very strong"
    assert cheak_password("123587QWRTYUKLjhgf") == "very strong"






