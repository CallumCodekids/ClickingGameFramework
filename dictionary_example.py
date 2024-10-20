words = "For dog  Bob 🤷 cat square"

letter_count_dict = {}

for letter in words:
    if letter in letter_count_dict:
        letter_count_dict[letter] = letter_count_dict[letter] +1
    else:
        letter_count_dict[letter] = 1
        


for key in letter_count_dict:
    print(key, letter_count_dict[key])