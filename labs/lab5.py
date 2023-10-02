word = str.upper(input("Enter a Word: "))

vowels = ['A', 'E', 'I', 'O', 'U']

vowel_count = 0
constanats = 0

for letter in word:
    if letter in vowels:
        vowel_count += 1
    else:
        constanats += 1

print(f"Your word has {constanats} constanatns and {vowel_count} vowels")