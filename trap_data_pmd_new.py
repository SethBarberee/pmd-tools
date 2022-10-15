import json
from typing import Dict

file = open('data.inc', 'r')
Lines = file.readlines()
probability_total = 0
num_floors = 0

master_dict = []
floor_dict = []
splitLine = []

printList = False  # signal when to export.. triggered when we hit all zeros line

# Build our master list of pokemon
for line in Lines:
    newLine = line.strip()

    # Skip over empty lines
    if not newLine:
        probability_total = 0  # reset our total
        continue

    splitLine += newLine.split(", ")

# print(splitLine)
# print(len(splitLine))

# Take 8 byte chunks
for i in range(0, len(splitLine), 40):
    # Slice the array in 8 chunks
    chunk = splitLine[i:i+40]
    probability_list = [0] * 20  # 20 diff traps
    print(chunk)

    # Zfill to get leading zero back to not fuck our percentages

    for trap in range(0, 40, 2):
        # print("chunk " + chunk[trap] + " " + chunk[trap + 1])
        percentage = chunk[trap + 1].lstrip("0x").zfill(2) + chunk[trap].lstrip("0x").zfill(2)
        # print("hex percentage: " + percentage)

        # print("Pre total: {}".format(probability_total))

        if not percentage:
            print("probability: 0")
        else:
            if int(percentage, 16) == 0:
                cur_percentage = 0
            else:
                cur_percentage = int(percentage, 16) - probability_total
            print("probability {}".format(cur_percentage))

            # Populate our list with the percentage
            probability_list[int(trap / 2)] = cur_percentage
            probability_total += cur_percentage

    # Export list to JSON
    print(probability_list)
    probability_total = 0

    # print("Cur total: {}".format(probability_total))

    pokemon_dict = {
        'Trip Trap': probability_list[0],
        'Mud Trap': probability_list[1],
        'Sticky Trap': probability_list[2],
        'Grimy Trap': probability_list[3],
        'Summon Trap': probability_list[4],
        'Pitfall Trap': probability_list[5],
        'Warp Trap': probability_list[6],
        'Gust Trap': probability_list[7],
        'Spin Trap': probability_list[8],
        'Slumber Trap': probability_list[9],
        'Slow Trap': probability_list[10],
        'Seal Trap': probability_list[11],
        'Poison Trap': probability_list[12],
        'Selfdestruct Trap': probability_list[13],
        'Explosion Trap': probability_list[14],
        'PP-Zero Trap': probability_list[15],
        'Chestnut Trap': probability_list[16],
        'Wonder Tile': probability_list[17],
        'Pokemon Trap': probability_list[18],
        'Spiked Tile': probability_list[19]
    }
    # print(floor_dict)
    name = "trap_found_out" + str(num_floors)
    master_dict.append({"name": name, "traps": pokemon_dict})
    num_floors += 1

file.close()

with open("traps_found.json", "w+") as fout:
    json.dump(master_dict, fout, indent=4, separators=(',', ': '))
