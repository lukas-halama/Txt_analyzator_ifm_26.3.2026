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

username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print("-" * 40)
    print("Welcome to the app, " + username)
    print("We have " + str(len(TEXTS)) + " texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program..")
    exit()

choice = input("Enter a number btw. 1 and 3 to select: ")

if not choice.isdigit():
    print("Invalid input, terminating..")
    exit()

choice_int = int(choice)
if choice_int < 1 or choice_int > 3:
    print("Choice out of range, terminating..")
    exit()

selected_text = TEXTS[choice_int - 1]

words = []
for word in selected_text.split():
    clean_word = word.strip(",.:;")
    words.append(clean_word)

title_case = 0
upper_case = 0
lower_case = 0
numeric_count = 0
total_sum = 0

for w in words:
    if w.istitle() and not w[0].isdigit():
        title_case = title_case + 1
        
    if w.isupper() and w.isalpha():
        upper_case = upper_case + 1
        
    if w.islower():
        lower_case = lower_case + 1
        
    if w.isdigit():
        numeric_count = numeric_count + 1
        total_sum = total_sum + int(w)

print("-" * 40)
print("There are " + str(len(words)) + " words in the selected text.")
print("There are " + str(title_case) + " titlecase words.")
print("There are " + str(upper_case) + " uppercase words.")
print("There are " + str(lower_case) + " lowercase words.")
print("There are " + str(numeric_count) + " numeric strings.")
print("The sum of all the numbers " + str(total_sum))
print("-" * 40)

counts = {}
for w in words:
    length = len(w)
    if length not in counts:
        counts[length] = 0
    counts[length] = counts[length] + 1

print("LEN | OCCURRENCES | NR.")
print("-" * 40)

for length in sorted(counts):
    stars = "*" * counts[length]
    print(str(length) + " | " + stars + " | " + str(counts[length]))
