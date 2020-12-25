import csv
import random
import math

# This CSV generator is going to randomly generate different units
# Running this data will hopefully reflect some preset rules I'm going to encode (i.e Having Nightmare monsters give more gold than others)
with open('./units.csv', 'w', newline='') as f:
    unitWriter = csv.writer(f)

    unitWriter.writerow(
        ['Type', 'Element', 'MaxHealth', 'GoldOnKill', 'Level', ])

    unitTypes = ['Dragon', 'Goblin', 'Demon',
                 'Wizard', 'Elf', 'Troll', 'Titan']
    unitElements = ['Fire', 'Ice', 'Water', 'Air',
                    'Lightning', 'Ash', 'Nightmare', 'Earth']

    i = 0

    while(i < 100):
        goldConstant = 1.565

        randomType = random.choice(unitTypes)
        randomElement = random.choice(unitElements)
        randomLevel = random.randint(1, 100)

        unitGold = math.floor(goldConstant * (randomLevel * 14))

        unitHealth = 10 * (randomLevel * 22)

        print(randomType)
        unitWriter.writerow(
            [randomType, randomElement, unitHealth, unitGold, randomLevel])
        i += 1
