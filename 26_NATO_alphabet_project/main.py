import pandas as pd

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (_, row) in alphabet_df.iterrows()}


def generate_phonetic() -> None:
    letters = input("Enter a word: ")
    try:
        output = [alphabet_dict[letter.upper()] for letter in letters]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # Call again recursively
    else:
        print(output)


generate_phonetic()
