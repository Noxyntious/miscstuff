# komentář. text za znakem # nebude považován jako kód, ale text.

promennaStr = "text" # určí proměnnou s typem řetězec (string), a textem "text"
promennaInt = 3 # určí promennou s typem celého čísla (integer), a hodnotou 3.
# DŮLEŽITÉ: v typu Int není možné použít desetinné číslo.
promennaFloat = 3.0 # určí proměnnou s typem desetinného čísla (floating point), a hodnotou 3.0
# Důležité: Jméno proměnné nesouvisí s typem, typ určuje zadaná hodnota. # Pokud bych pojmenoval proměnnou "promennaInt" ale hodnota by byla "text", tak by typ byl string, a ne int.
promennaBool = True # určí proměnnou s typem true/false (boolean), a hodnotou True. DŮLEŽITÉ: musí být napsáno velkým písmenem.

print("text") # napíše do konzole text v uvozovkách.
print(promennaStr) # napíše do konzole hodnotu proměnné.
print(promennaInt) # Příkaz print umí napsat všechny typy proměnných, ne jenom string.

str(promennaInt) # Příkaz str převede jakýkoliv typ proměnné na string (řetězec)
str(promennaFloat) # Funguje též s floatem
str(promennaBool) # a s booleanem.

promennaIntvStr = "3"
int(promennaIntvStr) # Příkaz int převede typ string na integer. DŮLEŽITÉ: Příkaz jenom funguje pokud v proměnné je číslo, ne text.

input("Jak se máš?") # Příkaz input napíše do konzole zadaný text, a pak počká na odpověd z konzole.
currentUserMood = input("Jak se máš?") # Proměnná "currentUserMood" bude obsahovat odpověd z konzole, kterou napsal uživatel

# Python může být použitý jako kalkulačka, jednodušše zadáním příkladu.
vysledek = 1 + 1 # Proměnná "vysledek" bude obsahovat výsledek příkladu 1 + 1, neboli 2.

# If (pokud) podmínky
a = 2
b = 1
if (a > b):
    print("A je větší než B.")
# Podmínka if zkontroluje pravdivost inputu, a spustí kód.
# Pokud a je větší než b, neboli 2 je větší než 1, kód po dvojtečce se spustí, jinak se nic nestane.

# DŮLEŽITÉ: Vzhledem k tomu, že Python nepoužívá složené závorky {}, ale dvojtečky, je nutné mít kód správně formátovaný.
# if (a > b):
# print("A je větší než B.")
# Zde před příkazem print chybí TAB, takže kód nepujde.

# If podmínky 2: elif
if (b > a):
    print("B je větší než A.")
elif (a > b):
    print("A je větší než B.")
# Pokud první podmínka b > a není pravda, Python se posune na druhou podmínku, určen příkazem elif (else if).
# Pokud druhá podmínka je pravdivá, Python spustí kód u druhé podmínky. Pokud žádná není pravdivá, nic se nestane.

# If podminky 3: else
if (b > a):
    print("B je větší než A.")
elif (b == a):
    print("B se rovná A.")
else:
    print("Podmínka není pravda.")
# Pokud žádná z podmínek určených příkazy if nebo elif není pravda, Python spustí kód u příkazu else.

# While loopy
c = 1
while (c == 1):
    print("C se rovná 1.")
# Příkaz while bude dokola běžet kód, pokud podmínka je pravdivá. Nikdy nepřestane, dokud program je zavřen tlačítkem X nebo Ctrl+C.

