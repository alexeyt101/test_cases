from typing import List, Optional, Union


def find_index_of_first_zero(array: Union[str, List[int]]) -> Optional[int]:
    """Find an index where the first zero was found."""
    if not array:
        # do something if necessary
        return None

    for idx, elem in enumerate(array):
        if not int(elem):
            return idx
    return None


def test_find_index_of_first_zero(array, right_answer):
    result = find_index_of_first_zero(array)
    print(f'result: {result}, expected result: {right_answer}')
    assert result == right_answer, f'Error on test case with {array} {type(array)}: right answer: {right_answer}'


if __name__ == '__main__':
    test_list =  [
            ('1100', 2),
            ('', None),
            ('111', None),
            ('000', 0),
            ('111111111111111111111111100000000', 25),
            ([1, 1, 0, 0], 2),
            ([], None),
            ([1, 1, 1], None),
            ([0, 0, 0], 0),
        ]
    for array, answer in test_list:
        test_find_index_of_first_zero(array, answer)

# Также найти первое вхождение какого-то элемента в строку или список можно при помощи встроенного
# метода index(), однако нужно не забыть обработать исключениe, которое будет вызвано в случае
# отсутствия исходной подстроки или индекса массива.
