
if __name__ == '__main__':
    test_tuple = ("Temich", False, 444)


    name, is_brainlet, cost = test_tuple


    print(test_tuple[:2])
    print(name, is_brainlet)



    yo = "Igo"

    a, b, c = yo

    print(a, b, c)

    basic_courses = ("Docker", "Ansible", "Ceph")
    advanced_courses = ("Kubernetes База", "Kubernetes Мега", "1", "2", "3")

    print((basic_courses + advanced_courses)[1::3])