import os
import json


def load_students():
    """
    Загружает список студентов из файла
    :return: data json
    """
    students_rel_filename = 'data/students.json'
    rel_path_to_students_file = os.path.join(os.path.pardir, students_rel_filename)

    with open(rel_path_to_students_file, 'r', encoding='utf-8') as students_file:
        students_file_text = students_file.read()
        students_json = json.loads(students_file_text)

    return students_json


def load_professions():
    """
    Загружает список профессий из файла
    :return: data json
    """
    professions_rel_filename = 'data/professions.json'
    rel_path_to_professions_file = os.path.join(os.path.pardir, professions_rel_filename)

    with open(rel_path_to_professions_file, 'r', encoding='utf-8') as rofessions_file:
        professions_file_text = rofessions_file.read()
        professions_json = json.loads(professions_file_text)

    return professions_json


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    :param pk: int
    :return: dict
    """
    students_data_json = load_students()

    for row in students_data_json:
        if row["pk"] == pk:
            return row


def get_profession_by_title(title):
    """
    Получает словарь с инфо о профе по названию
    :param title: str
    :return: dict
    """
    professions_data_json = load_professions()

    for row in professions_data_json:
        if row["title"] == title:
            return row


def check_fitness(student, profession):
    """"
    Функция получает студента и профессию, возвращала бы словарь типа:
    {
        "has": ["Python", "Linux"],
        "lacks": ["Docker, SQL"],
        "fit_percent": 50
    }
    """
    student_json = get_student_by_pk(student)
    profession_json = get_profession_by_title(profession)

    student_skills = set(student_json["skills"])
    profession_skills = set(profession_json["skills"])

    student_fitness_has = profession_skills.intersection(student_skills)
    student_fitness_lack = profession_skills.difference(student_fitness_has)
    student_fitness_fit_percent = round(len(student_fitness_has) / len(profession_skills), 2) * 100

    return {"has": student_fitness_has, "lack": student_fitness_lack, "fit_percent": student_fitness_fit_percent}


load_students()

print(get_student_by_pk(1))
print(get_profession_by_title('Backend'))

print(check_fitness(1, 'Backend'))
