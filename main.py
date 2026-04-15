TEXTS = [
    '''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly 
    impressive topographic feature that rises sharply some 1000 feet above 
    Twin Creek Valley to an elevation of more than 7500 feet above sea level. 
    The butte is located just north of US 30 and the Union Pacific Railroad, 
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright red, purple, yellow and 
    gray beds of the Wasatch Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor and steepen abruptly. 
    Overlying them and extending to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, which are about 300 
    feet thick.''',
    '''The monument contains 8198 acres and protects a portion of the largest 
    deposit of freshwater fish fossils in the world. The richest fossil fish 
    deposits are found in multiple limestone layers, which lie some 100 feet 
    below the top of the butte. The fossils represent several varieties of 
    perch, as well as other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, garpike and stingray 
    are also present.'''
]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# 1. Přihlášení
username = input("username: ")
password = input("password: ")

if users.get(username) == password:
    print("-" * 40, f"Welcome to the app, {username}", 
          f"We have {len(TEXTS)} texts to be analyzed.", "-" * 40, sep="\n")
else:
    print("unregistered user, terminating the program..")
    exit()

# 2. Výběr textu
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not choice.isdigit() or not (1 <= int(choice) <= len(TEXTS)):
    print("Invalid input or choice out of range, terminating..")
    exit()

selected_text = TEXTS[int(choice) - 1]
words = [word.strip(",.:;") for word in selected_text.split()]

# 3. Analýza
title_case = sum(1 for w in words if w.istitle() and not w[0].isdigit())
upper_case = sum(1 for w in words if w.isupper() and w.isalpha())
lower_case = sum(1 for w in words if w.islower())
numeric_strings = [w for w in words if w.isdigit()]
total_sum = sum(int(n) for n in numeric_strings)

print("-" * 40)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {title_case} titlecase words.")
print(f"There are {upper_case} uppercase words.")
print(f"There are {lower_case} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {total_sum}")
print("-" * 40)

# 4. Graf
counts = {}
for w in words:
    length = len(w)
    counts[length] = counts.get(length, 0) + 1

print(f"{'LEN':<3}| {'OCCURRENCES':<15} |{'NR.':<3}")
print("-" * 40)
for length in sorted(counts):
    stars = "*" * counts[length]
    print(f"{length:>3}| {stars:<15} |{counts[length]}")