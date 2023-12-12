import pandas
game_is_on = True

while game_is_on:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    new_dic = {row.letter: row.code for (key, row) in data.iterrows()}

    name = input("Enter Name: ").upper()
    words_list = [new_dic[letter] for letter in name]
    print(words_list)
    t = input("\n\n\tWanna exit ? tap 'y' for yes ").lower()
    if t == "y":
        game_is_on = False
