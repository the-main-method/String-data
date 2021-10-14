vowels= ["a", "e", "i", "o", "u"]
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
putin = input("Enter a string: ")
no_of_vowels = 0
no_of_consnts = 0
char_count = 0
char_count_ns = 0
word_count = 0

for i in putin:
    char_count += 1

    if not i == " ":
        char_count_ns += 1

    if i.lower() in vowels:
        no_of_vowels += 1

    if i.upper() in consonants:
        no_of_consnts += 1

words = putin.split(" ")
word_count = len(words)
    

print(f"There are {char_count} characters, {char_count_ns} not counting spaces, {no_of_vowels} vowels, {no_of_consnts} consonants, and {word_count} words here.")

sec_putin = input("Do you want to run a function on the string? (yes / no): ")
if sec_putin.lower() == "yes":
    func_put = input("Type the function you need here: ")
    func_put = func_put.lower()
    params = func_put.split(" ")

    if func_put.find("count") == 0:
        print(func_put.count(func_put[6:]))
