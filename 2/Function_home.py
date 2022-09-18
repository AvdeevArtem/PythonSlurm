def get_rps_data():
    rps_values = list(int(num) for num in input().strip().split(';'))
    return sorted(rps_values)


def get_avgrps_and_median(rps_values):
    average_rps = sum(rps_values) / len(rps_values)
    quotient, remainder = divmod(len(rps_values), 2)
    median = rps_values[quotient] if remainder else sum(rps_values[quotient - 1:quotient + 1]) / 2
    return average_rps, median

def get_percentage_of_the_difference(average_rps, median):
    percentage_of_the_difference = (average_rps - median) / median * 100
    return percentage_of_the_difference

def get_load_status(percentage_of_the_difference):
    if percentage_of_the_difference > 25:
        return "Происходят скачки"
    elif percentage_of_the_difference < 0:
        return "Происходят снижения"
    else:
        return "Нагрузка стабильна"

def main():
    rps_values = get_rps_data()
    average_rps, median = get_avgrps_and_median(rps_values)
    percentage_of_the_difference = get_percentage_of_the_difference(average_rps, median)
    print(get_load_status(percentage_of_the_difference))

if __name__ == '__main__':
    main()