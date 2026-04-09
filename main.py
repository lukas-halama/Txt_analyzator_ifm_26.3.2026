from time import sleep

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

'''
+------+-------------+
| user | password |
+------+-------------+
| bob | 123 |
| ann | pass123 |
| mike | password123 |
| liz | pass123 |
+------+-------------+

'''
print("\n" + "-" * 31)
print("        TEXT ANALYZER v2")
print("-" * 31)
print("Uživatelé: bob, ann, mike, liz\n")

jmeno = input("username: ").strip().lower()
heslo = input("password: ").strip()
print("-" * 31)
sleep(1)
print("Welcome to the app, bob")
print(f"We have [{len(TEXTS)}] texts to be analyzed.")
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

if jmeno not in users:
    print("neplatné jméno")
    exit()



'''
# ...
7| * 1
8| *********** 11
9| *************** 15
10| ********* 9
11| ********** 10

'''


if users.get(jmeno) == heslo:
    print("vstup povolen")
else:
    print("neplatne heslo nebo jmeno")

def count_words(text):
    words = text.split()
    return len(words)

def count_titlecase(text):
    words = text.split()
    titlecase_count = sum(1 for word in words if word.istitle())
    return titlecase_count

def count_uppercase(text):
    words = text.split()
    uppercase_count = sum(1 for word in words if word.isupper())
    return uppercase_count

def count_numbers(text):
    words = text.split()
    number_count = sum(1 for word in words if word.isdigit())
    return number_count


def lowercase(text):
    words = text.split()
    lowercase_count = sum(1 for word in words if word.islower())
    return lowercase_count

def numeric_string(text):
    words = text.split()
    numeric_string_count = sum(1 for word in words if word.isnumeric())
    return numeric_string_count

def sum_numbers(text):
    words = text.split()
    total_sum = sum(int(word) for word in words if word.isdigit())
    return total_sum


def word_length_distribution(text):
    words = text.split()
    length_distribution = {}
    for word in words:
        length = len(word)
        if length in length_distribution:
            length_distribution[length] += 1
        else:
            length_distribution[length] = 1
    return length_distribution

result = count_words(TEXTS[0])
print(f"There are {result} words in the selected text.")

result = count_titlecase(TEXTS[0])
print(f"There are {result} titlecase words.")

result = count_uppercase(TEXTS[0])
print(f"There are {result} uppercase words.")

result = lowercase(TEXTS[0])
print(f"There are {result} lowercase words.")

result = count_numbers(TEXTS[0])
print(f"There are {result} numeric strings.")

result = sum_numbers(TEXTS[0])
print(f"The sum of all the numbers {result}")   


print('''----------------------------------------
LEN| OCCURRENCES |NR.
----------------------------------------''')

result = word_length_distribution(TEXTS[0])
for length in sorted(result.keys()):
    occurrences = '*' * result[length]
    print(f"{length}| {occurrences} |{result[length]}")






'''


----------------------------------------
There are 54 words in the selected text.
There are 11 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 4 numeric strings.
The sum of all the numbers 8540
----------------------------------------
LEN| OCCURRENCES |NR.
----------------------------------------
1|* |1
2|********** |10
3|***** |5
4|*********** |11
5|************ |12
6|*** |3
7|**** |4
8|***** |5
9|* |1
10|* |1
11|* |1






'''

'''1|* |1
2|********** |10
3|***** |5
4|*********** |11
5|************ |12
6|*** |3
7|**** |4
8|***** |5
9|* |1
10|* |1
11|* |1

'''