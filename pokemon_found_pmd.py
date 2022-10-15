import json


file = open('data.inc', 'r')
Lines = file.readlines()
probability_total = 0
num_floors = 0


floor_dict = []

printList = False # signal when to export.. triggered when we hit all zeros line

for line in Lines:
    newLine = line.strip()
    newLine = newLine.strip(".byte")

    # Skip over empty lines
    if not newLine:
        probability_total = 0 # reset our total
        continue

    splitLine = newLine.split(", ")

    if len(splitLine) != 8:
        print("ERROR: incorrect format")
        break


    # byte order
    # byte 0: species ID
    # byte 1: level
    # byte 2 - 3: percentage
    # byte 4 - 5: percentage
    # byte 6 - 7: always zero

    SpeciesID = splitLine[0].lstrip(" 0x")

    if not SpeciesID:
        # We catch our all 0 line here and skip it
        probability_total = 0 # reset our total
        printList = True # time to export our table
    else:
        # Sometimes overflow into next byte so check
        SpeciesTest = splitLine[1].lstrip("0x")
        SpeciesTest = int(SpeciesTest, 16)
        if SpeciesTest & 1:
            SpeciesID = "1" + SpeciesID
        #print("SpeciesID HEX: {}".format(SpeciesID))
        #print("species: {}".format(int(SpeciesID, 16)))

    level = splitLine[1].strip(" 0x")
    if printList:
        print("")
    else:
        if not level:
            print("level: 0")
        else:
            temp = '{:<04}'
            level = temp.format(level)
            print("LEVEL HEX: {}".format(level))
            level = int(level, 16) / 512
            #print("level: {}".format(level))

    # Use lstrip to only strip the beginning
    #print("PERCENT DEBUG: " + splitLine[3] + " " + splitLine[2])
    #print("PERCENT H: " + splitLine[3].lstrip("0x").zfill(2))
    #print("PERCENT L: " + splitLine[2].lstrip("0x").zfill(2))

    # Zfill to get leading zero back to not fuck our percentages
    percentage = splitLine[3].lstrip("0x").zfill(2) + splitLine[2].lstrip("0x").zfill(2)

    #print("Pre total: {}".format(probability_total))


    if not percentage:
        print("probability: 0")
    else:
        if int(percentage, 16) == 0:
            cur_percentage = 0
        else:
            cur_percentage = int(percentage, 16) - probability_total
        #print("perobability {}".format(cur_percentage))
        probability_total += cur_percentage

    #print("Cur total: {}".format(probability_total))

    if not printList:
        pokemon_dict = {
                'species': int(SpeciesID,16),
                'level': int(level),
                'probability': int(cur_percentage)
        }
        floor_dict.append(pokemon_dict)
    else:
        print(floor_dict)
        with open("pokemon_found_out" + str(num_floors) + ".json", "w+") as fout:
            json.dump(floor_dict, fout, indent = 4, separators=(',',': '))
        printList = False
        num_floors += 1
        floor_dict = []


file.close()

