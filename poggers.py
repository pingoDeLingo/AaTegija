import random
import sqlite3

sonad = []
count = 0
id = 1
blanks = ["-","-","-","-","-"]
letters = []
notletters = []


ühendus = sqlite3.connect('data.db')
c = ühendus.cursor()
number = random.randint(1,2315)
print(number)

with open("stuff.txt") as f:

    for line in f.readlines():
        line = line.strip()
        sonad.append(line)
        id += 1
        suva = c.execute("SELECT * FROM Wurtel WHERE ID = (?)", (number))
        
c.close
ühendus.commit()
ühendus.close()

# suvaline = random.choice(sonad).lower()
true = False

while count < 5:
    proov = input("Word please: ")
    if len(proov) == 5:
        for i in range(5):
            if proov == suvaline:
                print("U are so smarterst")
                true = True
                exit()
            elif proov[i] == suvaline[i] and true == False:
                blanks[i] = proov[i]
        for letter in proov:
            if letter not in letters and letter in suvaline:
                letters.append(letter)
            elif letter not in notletters and letter not in suvaline:
                notletters.append(letter)
        count += 1
        print("Answer includes: " + ",".join(letters))
        print("Answer doesn't include: " + ",".join(notletters))
        print("".join(blanks))
print(suvaline)
