def nearest_value(values: set, one: int) -> int:
    sorted_values = sorted(values)
    if one < min(sorted_values):
        return list(sorted_values)[0]
    prev_val = the_val = 0
    for i in sorted_values:
        val = one - i
        pos_val = val * -1
        if 0 >= val:
            if prev_val < pos_val:
                the_val = one - prev_val
                break
            if prev_val > pos_val:
                the_val = i
                break

            if pos_val == prev_val:
                the_val = one - prev_val
                break
        else:
            the_val=i
        prev_val=val
    return the_val


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
