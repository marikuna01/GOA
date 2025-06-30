word = input("შეიყვანე სიტყვა: ")
vowel_count = 0

for letter in word:
    if letter in "აეიოუ":
        vowel_count += 1

print("ხმოვანების რაოდენობაა:", vowel_count)