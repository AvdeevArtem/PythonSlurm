


if __name__ == '__main__':
    vendor = input()
    tv_height = int(input())
    tv_width = int(input())

    if vendor in ("Sony", "LG", "Samsung"):
        if tv_height <= 130 and tv_width <= 140:
            print("Подходит")
        else:
            print("Ok")
    else:
        print("Not ok")

