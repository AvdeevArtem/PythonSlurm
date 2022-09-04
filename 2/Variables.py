
if __name__ == '__main__':
    # Сколько нужно датацентров для 68796 контейнеров
    amount_data_centers = (68796 / 4) / (21 * 117)
    print(amount_data_centers)
    #print((68796 / 4) / (21 * 117))

    #Сколько останется свободной памяти на всех нодах в датацентрах
    total_unused_memory = (amount_data_centers * 21 * 16384) - (68796 * 30)
    print(total_unused_memory)
    #print((amount_data_centers * 21 * 16384) - (68796 * 30))

    #Разбивка по гб/мб
    unused_memory_in_gigabytes = total_unused_memory // 1024
    unused_memory_in_megabytes = total_unused_memory % 1024
    print(unused_memory_in_gigabytes)
    print(unused_memory_in_megabytes)
    #print(344568 // 1024)
    #print(344568 % 1024)

