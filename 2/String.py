
if __name__ == '__main__':
    name = "Temich"
    job = 'SRE'
    email = "avdeev@yoyoyoyo.cloud"

    who_am_i = name + " " + job
    who_am_i_2 = "My name is {}, i'm {}, email me on {}".format(name, job, email)
    who_am_i_f = f"My name is {name:>20}, i'm {job}, email me on {email}"
    print(name, job)
    print(who_am_i)
    print(who_am_i_2)
    print(who_am_i_f)

    pod_name = "Pod"
    replicaset_name = "Replicaset"
    kubernetes_structures_desc = f"Для объединения нескольких контейнеров в одну минимальную логическую единицу используется {pod_name}, в то время как {replicaset_name} контролирует количество реплик приложения"
    print(kubernetes_structures_desc)


    platform = "K8s"
    atomic_unit = "POD"

    what_about_kubernetes = f"Минимальной единицей {platform.replace('K8s', 'Kubernetes')} является {atomic_unit.lower()}"
    print(what_about_kubernetes)

    instruction_name = "Disaster recovery plan"
    print(instruction_name[9:-5])
    print(instruction_name[9:])
    print(instruction_name[:8])

