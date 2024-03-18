def squaring_numbers() -> None:
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [n * n for n in numbers]
    print(squared_numbers)


def filtering_even_numbers() -> None:
    list_of_strings = input("Please input some integers separated by commas").split(",")

    list_of_ints = [int(n) for n in list_of_strings]

    result = [n for n in list_of_ints if n % 2 == 0]

    print(result)


def common_numbers(file_1: str, file_2: str) -> None:
    with open(file_1, "r") as file:
        file_1_list = file.readlines()
    with open(file_2, "r") as file:
        file_2_list = file.readlines()

    result = [int(n) for n in file_1_list if n in file_2_list]
    print(result)


# squaring_numbers()
# filtering_even_numbers()
common_numbers("file1.txt", "file2.txt")
