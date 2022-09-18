def get_email_and_job_from_input():
    """
    Получение почты и должности сотрудника


    :return: почты и профессии сотрудника
    """
    email = input()
    if email == "":
        print("Ввод прерван")
        return None, None

    print("Введите профессию")
    job = input()

    return email, job


def get_system_info(job):
    if job == "Программист":
        return "СКВ", 1
    elif job == "Дизайнер":
        return "Иллюстратор", 3
    else:
        print("Ааааа")
        return None, None

def allow_access_to_user(email, system, access_attempts):
    for _ in range(access_attempts):
        print(f"{email} был выдан доступ в {system}")



def main():
    processed_employees = 0
    while processed_employees < 5:

        email, job = get_email_and_job_from_input()

        if email is None and job is None:
            break

        system, access_attempts = get_system_info(job)

        if system is None and access_attempts is None:
            allow_access_to_user(email, access_attempts=1, system="sanitary_engineering_room")
            continue


        allow_access_to_user(email, access_attempts=access_attempts, system=system)

        processed_employees += 1
        print(f"Было внесено {processed_employees} сотрудников, осталось {5 - processed_employees}")


        #system = None
        #access_attempts = None


if __name__ == '__main__':
    main()
