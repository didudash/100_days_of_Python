import pandas as pd

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (_, row) in alphabet_df.iterrows()}
letters = input("Enter a word: ")
output = [alphabet_dict[letter.upper()] for letter in letters]
print(output)
