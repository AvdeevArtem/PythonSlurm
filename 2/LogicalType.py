

if __name__ == '__main__':
    free_ram_amount = 200  # Количество свободной оперативной памяти в облачном кластере в мегабайтах
    app_replicas = 2  # Количество реплик приложения
    has_ram_overdraft = True  # Есть ли возможность использовать дополнительную оперативную память при исчерпании лимита
    balance = 10000  # Баланс лицевого счета в местной валюте

    is_enough_money = has_ram_overdraft and balance > 8000
    is_enough_memory = app_replicas * 150 <= free_ram_amount
    print(is_enough_memory)
    print(is_enough_money)
    print(is_enough_memory or is_enough_money)