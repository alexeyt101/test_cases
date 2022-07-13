from typing import Dict, List, Set


def get_presence_time(intervals: List[int]) -> Set[int]:
    """Get a time array when a person persenced on the lesson."""
    presence_time = set()

    ranges = [range(intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2)]
    for r in ranges:
        presence_time.update(r)
    
    return presence_time


def calculate_total_time_of_pupil_and_tutor(intervals_data: Dict[str, List[int]]) -> int:
    """Calculate total time when a pupil and a tutor in class together during the lesson."""
    common_presence = get_presence_time(intervals_data['lesson']) & \
                        get_presence_time(intervals_data['pupil']) & \
                        get_presence_time(intervals_data['tutor'])
    
    common_presence_time = len(common_presence)
    return common_presence_time

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = calculate_total_time_of_pupil_and_tutor(test['data'])
       print(f'test answer: {test_answer}, expected answer {test["answer"]}')
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

