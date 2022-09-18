if __name__ == '__main__':

    # rps_values = \
    #     (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116,
    #      '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330',
    #      7186,
    #      '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357,
    #      '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850,
    #      '12791',
    #      11288)
    input_data = None
    while input_data is None:
        input_data = list(int(num) for num in input().strip().split(';'))
        rps_values = input_data
        print(sorted(rps_values))

        average_rps = sum(rps_values) / len(rps_values)
        quotient, remainder = divmod(len(rps_values), 2)
        median = rps_values[quotient] if remainder else sum(rps_values[quotient - 1:quotient + 1]) / 2
        print(average_rps, median)
        percentage_of_the_difference = (average_rps - median) / median * 100
        print(percentage_of_the_difference)
        if percentage_of_the_difference > 25:
            print("Происходят скачки")
        elif percentage_of_the_difference < 0:
            print("Происходят снижения")
        else:
            print("Нагрузка стабильна")




