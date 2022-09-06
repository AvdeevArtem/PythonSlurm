if __name__ == '__main__':

    branch = str(input())
    test_successful = int(input())
    coverage = float(input())
    approves = int(input())

    is_first_condition_true = test_successful == 1 and coverage > 5
    is_second_condition_true = test_successful == 1 and coverage <= 5 and approves > 3

    if not branch.lower().capitalize() in ("Staging", "Development"):
        print(f"В ветке {branch} непроверенный код, пропускаем")
    elif is_second_condition_true or is_first_condition_true:
        print(f"Внимание! Код из {branch} отправлен в релиз!")
    else:
        print \
            (f"Код из {branch} с результатами тесты: {test_successful}, coverage: {coverage}%, approve: {approves} в релиз не попадает.")
