TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
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
complete = False
GRAF = "-"
registrovani_uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

while True:
    username = input("Prosím zadej své uživatelské jméno: ")
    password = input("Prosím zadej své heslo: ")
    if username in registrovani_uzivatele and password == registrovani_uzivatele[username]:
        print(username, password)
        break
    else:
        print("Špatné uživatelské jméno a heslo, je třeba zadat uživatelské jméno a heslo znovu.")
print("-" * 42)
vyber_textu = input("Vyber si text od 1 do 3: ")
text = int(vyber_textu)
pocet_slov = len(TEXTS[text - 1].split())
print("Počet slov v textu je: ", pocet_slov)
count = 0
count1 = 0
count2 = 0
count3 = 0

for word in TEXTS[text - 1].split():
    if word[0].isupper():
        count = count + 1

print("Počet slov v textu začínající velkým písmenem je : " + str(count))

for word1 in TEXTS[text - 1].split():
    if (word1.isupper()):
        count1 = count1 + 1
print("Počet slov v textu velkým písmenem je : " + str(count1))

for word2 in TEXTS[text - 1].split():
    if (word2.islower()):
        count2 = count2 + 1
print("Počet slov v textu malým písmenem je : " + str(count2))

for word3 in TEXTS[text - 1].split():
    if (word3.isdigit()):
        count3 = count3 + 1
print("Počet čísel je :" + str(count3))
print("-" * 42)
vyskyt_slov = {}
for slovo in TEXTS[text - 1].split():
    word_length = int(len(slovo))
    vyskyt_slov[word_length] = vyskyt_slov.get(word_length, 0) + 1
    utrideno = sorted(vyskyt_slov)

for item in utrideno:
    print("Slovo s počtem znaků ", item, vyskyt_slov[item] * GRAF, vyskyt_slov[item], "x")
print("-" * 42)
sum_digit = 0
for word3 in TEXTS[text - 1].split():
    if word3.isdigit() == True:
        z = int(word3)
        sum_digit = sum_digit + z

print("Suma všech čísel v textu je:", sum_digit)