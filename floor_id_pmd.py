import json


file = open('data.inc', 'r')
Lines = file.readlines()
num_floors = 0


floor_dict = []

printList = False # signal when to export.. triggered when we hit all zeros line

for line in Lines:
    newLine = line.strip()
    newLine = newLine.strip(".byte")

    # Skip over empty lines
    if not newLine:
        continue

    splitLine = newLine.split(", ")

    if len(splitLine) != 16:
        print("ERROR: incorrect format")
        break


    # byte order
    # byte 0 - 1: Main Data
    # byte 2 - 3: Pokemon
    # byte 4 - 5: Traps
    # byte 6 - 7: Items
    # byte 8 - 9: KecleonShop
    # byte 10 - 11: MonsterRoom
    # byte 12 - 13: Buried Items
    # byte 14 - 15: always zero

    #print(splitLine)
    #print("mainData H: {}".format(splitLine[1].lstrip("0x")))
    #print("mainData L: {}".format(splitLine[0].strip().lstrip("0x")))

    mainData = splitLine[1].lstrip("0x").zfill(2) + splitLine[0].strip().lstrip("0x").zfill(2)
    if not mainData:
        # We catch our all 0 line here and skip it
        printList = True # time to export our table
    else:
        #print("mainData HEX: {}".format(mainData))
        print("mainData: {}".format(int(mainData, 16)))


    pokemon = splitLine[3].lstrip("0x").zfill(2) + splitLine[2].lstrip("0x").zfill(2)
    if not pokemon:
        break
    else:
        #print("pokemon HEX: {}".format(pokemon))
        print("pokemon: {}".format(int(pokemon, 16)))

    traps = splitLine[5].lstrip("0x").zfill(2) + splitLine[4].lstrip("0x").zfill(2)
    if not traps:
        break
    else:
        #print("traps HEX: {}".format(traps))
        print("traps: {}".format(int(traps, 16)))

    items = splitLine[7].lstrip("0x").zfill(2) + splitLine[6].lstrip("0x").zfill(2)
    if not items:
        break
    else:
        #print("items HEX: {}".format(items))
        print("items: {}".format(int(items, 16)))

    kecleonShop = splitLine[9].lstrip("0x").zfill(2) + splitLine[8].lstrip("0x").zfill(2)
    if not kecleonShop:
        break
    else:
        #print("kecleonShop HEX: {}".format(kecleonShop))
        print("kecleonShop: {}".format(int(kecleonShop, 16)))

    monsterRoom = splitLine[11].lstrip("0x").zfill(2) + splitLine[10].lstrip("0x").zfill(2)
    if not monsterRoom:
        break
    else:
        #print("monsterRoom HEX: {}".format(monsterRoom))
        print("monsterRoom: {}".format(int(monsterRoom, 16)))

    buriedItems = splitLine[13].lstrip("0x").zfill(2) + splitLine[12].lstrip("0x").zfill(2)
    if not buriedItems:
        break
    else:
        #print("buriedItems HEX: {}".format(buriedItems))
        print("buriedItems: {}".format(int(buriedItems, 16)))

    print("")

    pokemon_dict = {
            'MainData': int(mainData,16),
            'Pokemon': int(pokemon, 16),
            'Traps': int(traps, 16),
            'Items': int(items, 16),
            'KecleonShop': int(kecleonShop, 16),
            'MonsterRoomItems': int(monsterRoom, 16),
            'BuriedItems': int(buriedItems, 16),
    }
    floor_dict.append(pokemon_dict)


file.close()
print(floor_dict)
with open("floor_id_out" + str(num_floors) + ".json", "w+") as fout:
    json.dump(floor_dict, fout, indent = 4, separators=(',',': '))

