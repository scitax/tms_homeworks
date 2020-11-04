import random

# creating a list of firstnames
name_list = ['Masha', 'Petia', 'Roma', 'Kira', 'Arina', 'Vasia', 'Olia', 'Vasia', 'Sahsa']
# creating a list of subjects
subject_list = ['physics', 'history', 'informatics']

subject_number = len(subject_list)
number_of_pupils = input('Enter a number of students')

# generating random students data
if number_of_pupils.isdigit():
    number_of_pupils = int(number_of_pupils)
    pupils = [
        {'Firstname': random.choice(name_list),
        'Group': random.randint(1, 50),
        'physics': random.randint(1, 10),
        'history': random.randint(1, 10),
        'informatics': random.randint(1, 10),
        }
        for temp_pupils_number in range(0, int(number_of_pupils))
    ]
else:
    print('Not an integer number of students')
print(pupils, '\n')

# #selecting studens with average mark more than 4 and printing their data
# best_students = [student_data for student_data in pupils
#                  if (student_data['physics'] + student_data['history'] + student_data['history'])
#                  / subject_number > 4
#                  ]
# print('studens with average more than 4')
# print(best_students)
#
# subject_average_dict = {}

#calculating average mark on every subject
# for current_subject in subject_list:
#     current_subject_mark_sum = 0
#     for student_data in pupils:
#         current_subject_mark_sum += student_data[current_subject]
#     current_subject_average_mark = current_subject_mark_sum / number_of_pupils
#     subject_average_dict[current_subject] = current_subject_average_mark
# print(subject_average_dict)

