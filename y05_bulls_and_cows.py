# inpired on https://leetcode.com/problems/bulls-and-cows/


def calculate_hint(secret, guess):
    bulls = 0
    cows = 0

    secret = list(secret)
    guess = list(guess)

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls = bulls + 1
            secret[i] = "_"
            guess[i] = "_"

    for i in range(len(secret)):
        for index, value in enumerate(secret):
            if guess[i] == value and value != "_":
                cows = cows + 1
                secret[index] = "_"
                break

    return str(bulls) + "A" + str(cows) + "B"


def first_given_example():
    secret = "1807"
    guess = "7810"

    expected_result = "1A3B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


def second_given_example():
    secret = "1123"
    guess = "0111"

    expected_result = "1A1B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


def first_example_from_wiki():
    secret = "9305"
    guess = "1234"

    expected_result = "0A1B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


def first_test_with_single_digit():
    secret = "1"
    guess = "1"

    expected_result = "1A0B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


def first_test_with_2_digits():
    secret = "11"
    guess = "10"

    expected_result = "1A0B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


def test_with_4_digits():
    secret = "1122"
    guess = "0001"

    expected_result = "0A1B"

    calculated_result = calculate_hint(secret, guess)

    assert calculated_result == expected_result


first_given_example()
second_given_example()
first_test_with_2_digits()
first_example_from_wiki()
first_test_with_single_digit()
test_with_4_digits()
