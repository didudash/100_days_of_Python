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


def dict_comprehension() -> None:
    sentence = input("Please input a sentence")
    result = {word: len(word) for word in sentence.split()}
    print(result)


def temperature_converter(weather_c: dict) -> None:
    weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
    print(weather_f)


squaring_numbers()
filtering_even_numbers()
common_numbers("file1.txt", "file2.txt")
dict_comprehension()
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
temperature_converter(weather_c)
