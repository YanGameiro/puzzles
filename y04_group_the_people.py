# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
def groupThePeople(groupSizes):

    final_response = [[]]

    person_id = 0
    for group_size in groupSizes:
        print(person_id)

        if person_id == 0:
            final_response[0].append(person_id)

        if person_id != 0:

            current_group = 0

            ideal_size = groupSizes[final_response[current_group][0]]

            ideal_size_matches = ideal_size == group_size
            group_is_full = len(final_response[current_group]) == group_size

            print("ideal_size", ideal_size)
            print("group_size", group_size)
            print("ideal_size_matches", ideal_size_matches)
            print("group_is_full", group_is_full)

            if ideal_size_matches and not group_is_full:
                print("~I will insert~")
                # insert in that group

            print("------------------------")

        person_id = person_id + 1

    return final_response
    # return [[5],[0,1,2],[3,4,6]]


def test_example_1():
    given = [3, 3, 3, 3, 3, 1, 3]
    expected = [[5], [0, 1, 2], [3, 4, 6]]
    print(groupThePeople(given))
    # assert groupThePeople(given) == expected


test_example_1()
