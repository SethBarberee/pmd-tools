import json


file = open('data.inc', 'r')
Lines = file.readlines()
num_floors = 0

floorLayout_H = 10
dungeonGenerationType = 10
tileset = 10
bgMusic = 10
weather = 10
Unknown_05 = 10
pokeDensity = 10
shopDensity = 10
MHDensity = 10
Unknown_09 = 10
stickyChance = 10
Unknown_11 = 10
hasTerrainPond = 10
hasTerrainTiles = 10
Unknown_14 = 10
itemDensity = 10
trapDensity = 10
floorNum = 10
eventFloor = 10
terrainDensity = 10
visibility = 10
maxPoke = 10
Unknown_24 = 10
Unknown_24_1 = 10
Unknown_24_2 = 10
Unknown_24_3 = 10


def singleByteRead(var, buffer, byteIdx, name):
    " Read a single byte from a list of bytes using an index "
    var = buffer[byteIdx].lstrip("0x").zfill(2)
    if var:
        #print(name +  " HEX: {}".format(var))
        # NOTE: help
        print(name + " : {}".format(int(var, 16)))
    return var

floor_dict = []

printList = False # signal when to export.. triggered when we hit all zeros line

for line in Lines:
    newLine = line.strip()
    newLine = newLine.strip(".byte")

    # Skip over empty lines
    if not newLine:
        continue

    splitLine = newLine.split(", ")

    if len(splitLine) != 28:
        print("ERROR: incorrect format")
        break


    # byte order
    # byte 0 - 1: Floor Layout
    # byte 2: tileset
    # byte 3: Background Music
    # byte 4: Weather
    # byte 5: Unknown
    # byte 6: Pokemon Density
    # byte 7: Shop Density
    # byte 8: Monster House Density
    # byte 9: Unknown
    # byte 10: Item Usability
    # byte 12: hasTerrainPond
    # byte 13: hasTerrainTiles
    # byte 15: Item Density
    # byte 16: Trap Density
    # byte 17: Floor Number
    # byte 18: Event Floor
    # byte 21: Terrain Density
    # byte 22: Visibility
    # byte 23: Max Poke Found
    # byte 24 - 27: Unknown (PMDe says its an int)

    print(splitLine)
    #print("floorLayout H: {}".format(splitLine[1].lstrip("0x")))
    #print("floorLayout L: {}".format(splitLine[0].strip().lstrip("0x")))

    floorLayout = splitLine[1].lstrip("0x").zfill(2) + splitLine[0].strip().lstrip("0x").zfill(2)
    if not floorLayout:
        # We catch our all 0 line here and skip it
        printList = True # time to export our table
    else:
        #print("floorLayout HEX: {}".format(floorLayout))
        print("floorLayout: {}".format(int(floorLayout, 16)))

    dungeonGenerationType = singleByteRead(dungeonGenerationType, splitLine, 0, "dungeonGenerationType")
    floorLayout_H = singleByteRead(floorLayout_H, splitLine, 1, "floorLayout_H")

    tileset = singleByteRead(tileset, splitLine, 2, "tileset")
    bgMusic = singleByteRead(bgMusic, splitLine, 3, "bgMusic")
    weather = singleByteRead(weather, splitLine, 4, "weather")
    Unknown_05 = singleByteRead(Unknown_05, splitLine, 5, "Unknown_05")
    pokeDensity = singleByteRead(pokeDensity, splitLine, 6, "pokeDensity")
    shopDensity = singleByteRead(shopDensity, splitLine, 7, "shopDensity")
    MHDensity = singleByteRead(MHDensity, splitLine, 8, "MHDensity")
    Unknown_09 = singleByteRead(Unknown_09, splitLine, 9, "Unknown_09")
    stickyChance = singleByteRead(stickyChance, splitLine, 10, "stickyChance")
    Unknown_11 = singleByteRead(Unknown_11, splitLine, 11, "Unknown_11")
    hasTerrainPond = singleByteRead(hasTerrainPond, splitLine, 12, "hasTerrainPond")
    hasTerrainTiles = singleByteRead(hasTerrainTiles, splitLine, 13, "hasTerrainTiles")
    Unknown_14 = singleByteRead(Unknown_14, splitLine, 14, "Unknown_14")
    itemDensity = singleByteRead(itemDensity, splitLine, 15, "itemDensity")
    trapDensity = singleByteRead(trapDensity, splitLine, 16, "trapDensity")
    floorNum = singleByteRead(floorNum, splitLine, 17, "floorNum")
    eventFloor = singleByteRead(eventFloor, splitLine, 18, "eventFloor")

    crossings = splitLine[20].lstrip("0x").zfill(2) + splitLine[19].strip().lstrip("0x").zfill(2)
    if crossings:
        #print("crossings HEX: {}".format(crossings))
        print("crossings: {}".format(int(crossings, 16)))

    terrainDensity = singleByteRead(terrainDensity, splitLine, 21, "terrainDensity")
    visibility = singleByteRead(visibility, splitLine, 22, "visibility")
    maxPoke = singleByteRead(maxPoke, splitLine, 23, "maxPoke")
    Unknown_24 = singleByteRead(Unknown_24, splitLine, 24, "Unknown_24")
    Unknown_24_1 = singleByteRead(Unknown_24_1, splitLine, 25, "Unknown_24_1")
    Unknown_24_2 = singleByteRead(Unknown_24_2, splitLine, 26, "Unknown_24_2")
    Unknown_24_3 = singleByteRead(Unknown_24_3, splitLine, 27, "Unknown_24_3")


    print("")

    pokemon_dict = {
        'dungeonGenerationType': int(dungeonGenerationType, 16),
        'floorLayout_H'        : int(floorLayout_H, 16),
        'tileset'              : int(tileset, 16),
        'bgMusic'              : int(bgMusic, 16),
        'weather'              : int(weather, 16),
        'Unknown_05'           : int(Unknown_05, 16),
        'pokeDensity'          : int(pokeDensity, 16),
        'shopDensity'          : int(shopDensity, 16),
        'MHDensity'            : int(MHDensity, 16),
        'Unknown_09'           : int(Unknown_09, 16),
        'stickyChance'         : int(stickyChance, 16),
        'Unknown_11'           : int(Unknown_11, 16),
        'hasTerrainPond'       : int(hasTerrainPond, 16),
        'hasTerrainTiles'      : int(hasTerrainTiles, 16),
        'Unknown_14'           : int(Unknown_14, 16),
        'itemDensity'          : int(itemDensity, 16),
        'trapDensity'          : int(trapDensity, 16),
        'floorNum'             : int(floorNum, 16),
        'eventFloor'           : int(eventFloor, 16),
        'crossings'            : int(crossings, 16),
        'terrainDensity'       : int(terrainDensity, 16),
        'visibility'           : int(visibility, 16),
        'maxPoke'              : int(maxPoke, 16),
        'Unknown_24'           : int(Unknown_24, 16),
        'Unknown_24_1'         : int(Unknown_24_1, 16),
        'Unknown_24_2'         : int(Unknown_24_2, 16),
        'Unknown_24_3'         : int(Unknown_24_3, 16),
    }
    floor_dict.append(pokemon_dict)


file.close()
print(floor_dict)
with open("main_data_out" + str(num_floors) + ".json", "w+") as fout:
    json.dump(floor_dict, fout, indent = 4, separators=(',',': '))

