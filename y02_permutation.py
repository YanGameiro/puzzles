# Daily Coding Problem: Problem #206 [Easy]
# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
# Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

def swap(orig, permutation):

    result = []

    for p in permutation:

        if p >= len(orig):
            return []

        if p < 0:
            return []

        result.append(orig[p])
    
    return result

def test_given_permutation():
    result = swap(["a", "b", "c"], [2, 1, 0])
    expected = ["c", "b", "a"]
    assert expected == result

def test_another_permutation():
    result = swap(["a", "b", "c"], [0, 2, 1])
    expected = ["a", "c", "b"]
    assert expected == result

def test_permutation_with_more_elements():
    result = swap(["a", "b", "c", "d", "e"], [3, 1, 4, 0, 2])
    expected = ["d", "b", "e", "a", "c"]
    assert expected == result

def test_empty_orig():
    result = swap([], [3, 1, 4, 0, 2])
    expected = []
    assert expected == result

def test_empty_permutation():
    result = swap(["a", "b", "c"], [])
    expected = []
    assert expected == result

def test_negative_permutation():
    result = swap(["a", "b", "c"], [0, 1, -2])
    expected = []
    assert expected == result

test_given_permutation()
test_another_permutation()
test_permutation_with_more_elements()
test_empty_orig()
test_empty_permutation()
test_negative_permutation()