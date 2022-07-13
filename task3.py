def appearance(intervals):
    lessonstart = intervals['lesson'][0]
    lessonend = intervals['lesson'][1]
    pupilinside = []
    for i in range(0, len(intervals['pupil']) - 1, 2):
        pupilstart = intervals['pupil'][i]
        pupilend = intervals['pupil'][i+1]
        if (pupilstart >= lessonstart and pupilend <= lessonend):
            pupilinside.append(pupilstart)
            pupilinside.append(pupilend)
        elif (pupilstart <= lessonstart and pupilend <= lessonend):
            pupilinside.append(lessonstart)
            pupilinside.append(pupilend)
        elif (pupilstart >= lessonstart and pupilend >= lessonend):
            pupilinside.append(pupilstart)
            pupilinside.append(lessonend)
        elif (pupilstart <= lessonstart and pupilend >= lessonend):
            pupilinside.append(lessonstart)
            pupilinside.append(lessonend)
        else:
            pass

    tutors_and_pupils_inside = []

    for i in range(0, len(pupilinside) - 1, 2):
        pupilstart = pupilinside[i]
        pupilend = pupilinside[i + 1]
        for j in range(0, len(intervals['tutor']) - 1, 2):
            tutorstart = intervals['tutor'][j]
            tutorend = intervals['tutor'][j + 1]
            if tutorstart >= pupilend:
                break
            if (tutorstart >= pupilstart and tutorend <= pupilend):
                tutors_and_pupils_inside.append(tutorstart)
                tutors_and_pupils_inside.append(tutorend)
            elif (tutorstart <= pupilstart and tutorend <= pupilend):
                tutors_and_pupils_inside.append(pupilstart)
                tutors_and_pupils_inside.append(tutorend)
            elif (tutorstart >= pupilstart and tutorend >= pupilend):
                tutors_and_pupils_inside.append(tutorstart)
                tutors_and_pupils_inside.append(pupilend)
            elif (tutorstart <= pupilstart and tutorend >= pupilend):
                tutors_and_pupils_inside.append(pupilstart)
                tutors_and_pupils_inside.append(pupilend)
            else:
                break

    answer = 0
    for g in range(0, len(tutors_and_pupils_inside) - 1, 2):
        togetherstart = tutors_and_pupils_inside[g]
        togetherend = tutors_and_pupils_inside[g+1]
        answer += togetherend - togetherstart
    return answer


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    #В этом кейсе студент зашел во вторую сессию до того как выщел из первой

    #{'data': {'lesson': [1594702800, 1594706400],
    #         'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #         'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #'answer': 3577
    #},
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])

       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
       print(f'Test complete')


