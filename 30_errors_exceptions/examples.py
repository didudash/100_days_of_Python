def index_error_handling() -> None:
    fruits = ["Apple", "Pear", "Orange"]

    def make_pie(index):
        try:
            fruit = fruits[index]
        except IndexError:
            print("fruit pie")
        else:
            print(fruit + " pie")

    make_pie(4)


def key_error_handling() -> None:
    facebook_posts = [
        {"Likes": 21, "Comments": 2},
        {"Likes": 13, "Comments": 2, "Shares": 1},
        {"Likes": 33, "Comments": 8, "Shares": 3},
        {"Comments": 4, "Shares": 2},
        {"Comments": 1, "Shares": 1},
        {"Likes": 19, "Comments": 3},
    ]

    try:
        total_likes = 0
        for post in facebook_posts:
            total_likes = total_likes + post["Likes"]
    except KeyError:
        pass
    finally:
        print(total_likes)


# index_error_handling()
# key_error_handling()
