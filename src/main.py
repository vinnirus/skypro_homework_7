import skypro_functions


def is_user_input_correct(data_json, dict_key, user_input):
    for row in data_json:
        if row[dict_key] == user_input:
            return True

    return False


if __name__ == '__main__':
    pk_student = int(input('Введите номер студента\n'))

    students_data_json = skypro_functions.load_students()

    if not is_user_input_correct(students_data_json, "pk", pk_student):
        print('У нас нет такого студента')

    else:
        student_full_name = skypro_functions.get_student_by_pk(pk_student)["full_name"]
        print(f'Студент {student_full_name}')
        print(f'Знает {skypro_functions.get_student_by_pk(pk_student)["skills"]}')

        profession_name = input(f'Введите специальность для оценки студента {student_full_name}\n')

        professions_data_json = skypro_functions.load_professions()

        if not is_user_input_correct(professions_data_json, "title", profession_name):
            print('У нас нет такой специальности')

        else:
            student_fitness = skypro_functions.check_fitness(pk_student, profession_name)
            print(f'Пригодность {student_fitness["fit_percent"]}')
            print(f'{student_full_name} знает {student_fitness["has"]}')
            print(f'{student_full_name} не знает {student_fitness["lack"]}')
