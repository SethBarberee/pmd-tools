import json
from typing import Dict

file = open('data.inc', 'r')
Lines = file.readlines()
probability_total = 0
num_floors = 112


master_dict = []
floor_dict = []
splitLine = []

printList = False  # signal when to export.. triggered when we hit all zeros line

species_map: Dict[int, str] = {}
index = 0
species_list = [
  'SPECIES_NONE',
  'SPECIES_BULBASAUR',
  'SPECIES_IVYSAUR',
  'SPECIES_VENUSAUR',
  'SPECIES_CHARMANDER',
  'SPECIES_CHARMELEON',
  'SPECIES_CHARIZARD',
  'SPECIES_SQUIRTLE',
  'SPECIES_WARTORTLE',
  'SPECIES_BLASTOISE',
  'SPECIES_CATERPIE',
  'SPECIES_METAPOD',
  'SPECIES_BUTTERFREE',
  'SPECIES_WEEDLE',
  'SPECIES_KAKUNA',
  'SPECIES_BEEDRILL',
  'SPECIES_PIDGEY',
  'SPECIES_PIDGEOTTO',
  'SPECIES_PIDGEOT',
  'SPECIES_RATTATA',
  'SPECIES_RATICATE',
  'SPECIES_SPEAROW',
  'SPECIES_FEAROW',
  'SPECIES_EKANS',
  'SPECIES_ARBOK',
  'SPECIES_PIKACHU',
  'SPECIES_RAICHU',
  'SPECIES_SANDSHREW',
  'SPECIES_SANDSLASH',
  'SPECIES_NIDORAN♀',
  'SPECIES_NIDORINA',
  'SPECIES_NIDOQUEEN',
  'SPECIES_NIDORAN♂',
  'SPECIES_NIDORINO',
  'SPECIES_NIDOKING',
  'SPECIES_CLEFAIRY',
  'SPECIES_CLEFABLE',
  'SPECIES_VULPIX',
  'SPECIES_NINETALES',
  'SPECIES_JIGGLYPUFF',
  'SPECIES_WIGGLYTUFF',
  'SPECIES_ZUBAT',
  'SPECIES_GOLBAT',
  'SPECIES_ODDISH',
  'SPECIES_GLOOM',
  'SPECIES_VILEPLUME',
  'SPECIES_PARAS',
  'SPECIES_PARASECT',
  'SPECIES_VENONAT',
  'SPECIES_VENOMOTH',
  'SPECIES_DIGLETT',
  'SPECIES_DUGTRIO',
  'SPECIES_MEOWTH',
  'SPECIES_PERSIAN',
  'SPECIES_PSYDUCK',
  'SPECIES_GOLDUCK',
  'SPECIES_MANKEY',
  'SPECIES_PRIMEAPE',
  'SPECIES_GROWLITHE',
  'SPECIES_ARCANINE',
  'SPECIES_POLIWAG',
  'SPECIES_POLIWHIRL',
  'SPECIES_POLIWRATH',
  'SPECIES_ABRA',
  'SPECIES_KADABRA',
  'SPECIES_ALAKAZAM',
  'SPECIES_MACHOP',
  'SPECIES_MACHOKE',
  'SPECIES_MACHAMP',
  'SPECIES_BELLSPROUT',
  'SPECIES_WEEPINBELL',
  'SPECIES_VICTREEBEL',
  'SPECIES_TENTACOOL',
  'SPECIES_TENTACRUEL',
  'SPECIES_GEODUDE',
  'SPECIES_GRAVELER',
  'SPECIES_GOLEM',
  'SPECIES_PONYTA',
  'SPECIES_RAPIDASH',
  'SPECIES_SLOWPOKE',
  'SPECIES_SLOWBRO',
  'SPECIES_MAGNEMITE',
  'SPECIES_MAGNETON',
  'SPECIES_FARFETCH',
  'SPECIES_DODUO',
  'SPECIES_DODRIO',
  'SPECIES_SEEL',
  'SPECIES_DEWGONG',
  'SPECIES_GRIMER',
  'SPECIES_MUK',
  'SPECIES_SHELLDER',
  'SPECIES_CLOYSTER',
  'SPECIES_GASTLY',
  'SPECIES_HAUNTER',
  'SPECIES_GENGAR',
  'SPECIES_ONIX',
  'SPECIES_DROWZEE',
  'SPECIES_HYPNO',
  'SPECIES_KRABBY',
  'SPECIES_KINGLER',
  'SPECIES_VOLTORB',
  'SPECIES_ELECTRODE',
  'SPECIES_EXEGGCUTE',
  'SPECIES_EXEGGUTOR',
  'SPECIES_CUBONE',
  'SPECIES_MAROWAK',
  'SPECIES_HITMONLEE',
  'SPECIES_HITMONCHAN',
  'SPECIES_LICKITUNG',
  'SPECIES_KOFFING',
  'SPECIES_WEEZING',
  'SPECIES_RHYHORN',
  'SPECIES_RHYDON',
  'SPECIES_CHANSEY',
  'SPECIES_TANGELA',
  'SPECIES_KANGASKHAN',
  'SPECIES_HORSEA',
  'SPECIES_SEADRA',
  'SPECIES_GOLDEEN',
  'SPECIES_SEAKING',
  'SPECIES_STARYU',
  'SPECIES_STARMIE',
  'SPECIES_MR. MIME',
  'SPECIES_SCYTHER',
  'SPECIES_JYNX',
  'SPECIES_ELECTABUZZ',
  'SPECIES_MAGMAR',
  'SPECIES_PINSIR',
  'SPECIES_TAUROS',
  'SPECIES_MAGIKARP',
  'SPECIES_GYARADOS',
  'SPECIES_LAPRAS',
  'SPECIES_DITTO',
  'SPECIES_EEVEE',
  'SPECIES_VAPOREON',
  'SPECIES_JOLTEON',
  'SPECIES_FLAREON',
  'SPECIES_PORYGON',
  'SPECIES_OMANYTE',
  'SPECIES_OMASTAR',
  'SPECIES_KABUTO',
  'SPECIES_KABUTOPS',
  'SPECIES_AERODACTYL',
  'SPECIES_SNORLAX',
  'SPECIES_ARTICUNO',
  'SPECIES_ZAPDOS',
  'SPECIES_MOLTRES',
  'SPECIES_DRATINI',
  'SPECIES_DRAGONAIR',
  'SPECIES_DRAGONITE',
  'SPECIES_MEWTWO',
  'SPECIES_MEW',
  'SPECIES_CHIKORITA',
  'SPECIES_BAYLEEF',
  'SPECIES_MEGANIUM',
  'SPECIES_CYNDAQUIL',
  'SPECIES_QUILAVA',
  'SPECIES_TYPHLOSION',
  'SPECIES_TOTODILE',
  'SPECIES_CROCONAW',
  'SPECIES_FERALIGATR',
  'SPECIES_SENTRET',
  'SPECIES_FURRET',
  'SPECIES_HOOTHOOT',
  'SPECIES_NOCTOWL',
  'SPECIES_LEDYBA',
  'SPECIES_LEDIAN',
  'SPECIES_SPINARAK',
  'SPECIES_ARIADOS',
  'SPECIES_CROBAT',
  'SPECIES_CHINCHOU',
  'SPECIES_LANTURN',
  'SPECIES_PICHU',
  'SPECIES_CLEFFA',
  'SPECIES_IGGLYBUFF',
  'SPECIES_TOGEPI',
  'SPECIES_TOGETIC',
  'SPECIES_NATU',
  'SPECIES_XATU',
  'SPECIES_MAREEP',
  'SPECIES_FLAAFFY',
  'SPECIES_AMPHAROS',
  'SPECIES_BELLOSSOM',
  'SPECIES_MARILL',
  'SPECIES_AZUMARILL',
  'SPECIES_SUDOWOODO',
  'SPECIES_POLITOED',
  'SPECIES_HOPPIP',
  'SPECIES_SKIPLOOM',
  'SPECIES_JUMPLUFF',
  'SPECIES_AIPOM',
  'SPECIES_SUNKERN',
  'SPECIES_SUNFLORA',
  'SPECIES_YANMA',
  'SPECIES_WOOPER',
  'SPECIES_QUAGSIRE',
  'SPECIES_ESPEON',
  'SPECIES_UMBREON',
  'SPECIES_MURKROW',
  'SPECIES_SLOWKING',
  'SPECIES_MISDREAVUS',
  'SPECIES_UNOWN_A',
  'SPECIES_UNOWN_B',
  'SPECIES_UNOWN_C',
  'SPECIES_UNOWN_D',
  'SPECIES_UNOWN_E',
  'SPECIES_UNOWN_F',
  'SPECIES_UNOWN_G',
  'SPECIES_UNOWN_H',
  'SPECIES_UNOWN_I',
  'SPECIES_UNOWN_J',
  'SPECIES_UNOWN_K',
  'SPECIES_UNOWN_L',
  'SPECIES_UNOWN_M',
  'SPECIES_UNOWN_N',
  'SPECIES_UNOWN_O',
  'SPECIES_UNOWN_P',
  'SPECIES_UNOWN_Q',
  'SPECIES_UNOWN_R',
  'SPECIES_UNOWN_S',
  'SPECIES_UNOWN_T',
  'SPECIES_UNOWN_U',
  'SPECIES_UNOWN_V',
  'SPECIES_UNOWN_W',
  'SPECIES_UNOWN_X',
  'SPECIES_UNOWN_Y',
  'SPECIES_UNOWN_Z',
  'SPECIES_WOBBUFFET',
  'SPECIES_GIRAFARIG',
  'SPECIES_PINECO',
  'SPECIES_FORRETRESS',
  'SPECIES_DUNSPARCE',
  'SPECIES_GLIGAR',
  'SPECIES_STEELIX',
  'SPECIES_SNUBBULL',
  'SPECIES_GRANBULL',
  'SPECIES_QWILFISH',
  'SPECIES_SCIZOR',
  'SPECIES_SHUCKLE',
  'SPECIES_HERACROSS',
  'SPECIES_SNEASEL',
  'SPECIES_TEDDIURSA',
  'SPECIES_URSARING',
  'SPECIES_SLUGMA',
  'SPECIES_MAGCARGO',
  'SPECIES_SWINUB',
  'SPECIES_PILOSWINE',
  'SPECIES_CORSOLA',
  'SPECIES_REMORAID',
  'SPECIES_OCTILLERY',
  'SPECIES_DELIBIRD',
  'SPECIES_MANTINE',
  'SPECIES_SKARMORY',
  'SPECIES_HOUNDOUR',
  'SPECIES_HOUNDOOM',
  'SPECIES_KINGDRA',
  'SPECIES_PHANPY',
  'SPECIES_DONPHAN',
  'SPECIES_PORYGON2',
  'SPECIES_STANTLER',
  'SPECIES_SMEARGLE',
  'SPECIES_TYROGUE',
  'SPECIES_HITMONTOP',
  'SPECIES_SMOOCHUM',
  'SPECIES_ELEKID',
  'SPECIES_MAGBY',
  'SPECIES_MILTANK',
  'SPECIES_BLISSEY',
  'SPECIES_RAIKOU',
  'SPECIES_ENTEI',
  'SPECIES_SUICUNE',
  'SPECIES_LARVITAR',
  'SPECIES_PUPITAR',
  'SPECIES_TYRANITAR',
  'SPECIES_LUGIA',
  'SPECIES_HO_OH',
  'SPECIES_CELEBI',
  'SPECIES_TREECKO',
  'SPECIES_GROVYLE',
  'SPECIES_SCEPTILE',
  'SPECIES_TORCHIC',
  'SPECIES_COMBUSKEN',
  'SPECIES_BLAZIKEN',
  'SPECIES_MUDKIP',
  'SPECIES_MARSHTOMP',
  'SPECIES_SWAMPERT',
  'SPECIES_POOCHYENA',
  'SPECIES_MIGHTYENA',
  'SPECIES_ZIGZAGOON',
  'SPECIES_LINOONE',
  'SPECIES_WURMPLE',
  'SPECIES_SILCOON',
  'SPECIES_BEAUTIFLY',
  'SPECIES_CASCOON',
  'SPECIES_DUSTOX',
  'SPECIES_LOTAD',
  'SPECIES_LOMBRE',
  'SPECIES_LUDICOLO',
  'SPECIES_SEEDOT',
  'SPECIES_NUZLEAF',
  'SPECIES_SHIFTRY',
  'SPECIES_TAILLOW',
  'SPECIES_SWELLOW',
  'SPECIES_WINGULL',
  'SPECIES_PELIPPER',
  'SPECIES_RALTS',
  'SPECIES_KIRLIA',
  'SPECIES_GARDEVOIR',
  'SPECIES_SURSKIT',
  'SPECIES_MASQUERAIN',
  'SPECIES_SHROOMISH',
  'SPECIES_BRELOOM',
  'SPECIES_SLAKOTH',
  'SPECIES_VIGOROTH',
  'SPECIES_SLAKING',
  'SPECIES_NINCADA',
  'SPECIES_NINJASK',
  'SPECIES_SHEDINJA',
  'SPECIES_WHISMUR',
  'SPECIES_LOUDRED',
  'SPECIES_EXPLOUD',
  'SPECIES_MAKUHITA',
  'SPECIES_HARIYAMA',
  'SPECIES_AZURILL',
  'SPECIES_NOSEPASS',
  'SPECIES_SKITTY',
  'SPECIES_DELCATTY',
  'SPECIES_SABLEYE',
  'SPECIES_MAWILE',
  'SPECIES_ARON',
  'SPECIES_LAIRON',
  'SPECIES_AGGRON',
  'SPECIES_MEDITITE',
  'SPECIES_MEDICHAM',
  'SPECIES_ELECTRIKE',
  'SPECIES_MANECTRIC',
  'SPECIES_PLUSLE',
  'SPECIES_MINUN',
  'SPECIES_VOLBEAT',
  'SPECIES_ILLUMISE',
  'SPECIES_ROSELIA',
  'SPECIES_GULPIN',
  'SPECIES_SWALOT',
  'SPECIES_CARVANHA',
  'SPECIES_SHARPEDO',
  'SPECIES_WAILMER',
  'SPECIES_WAILORD',
  'SPECIES_NUMEL',
  'SPECIES_CAMERUPT',
  'SPECIES_TORKOAL',
  'SPECIES_SPOINK',
  'SPECIES_GRUMPIG',
  'SPECIES_SPINDA',
  'SPECIES_TRAPINCH',
  'SPECIES_VIBRAVA',
  'SPECIES_FLYGON',
  'SPECIES_CACNEA',
  'SPECIES_CACTURNE',
  'SPECIES_SWABLU',
  'SPECIES_ALTARIA',
  'SPECIES_ZANGOOSE',
  'SPECIES_SEVIPER',
  'SPECIES_LUNATONE',
  'SPECIES_SOLROCK',
  'SPECIES_BARBOACH',
  'SPECIES_WHISCASH',
  'SPECIES_CORPHISH',
  'SPECIES_CRAWDAUNT',
  'SPECIES_BALTOY',
  'SPECIES_CLAYDOL',
  'SPECIES_LILEEP',
  'SPECIES_CRADILY',
  'SPECIES_ANORITH',
  'SPECIES_ARMALDO',
  'SPECIES_FEEBAS',
  'SPECIES_MILOTIC',
  'SPECIES_CASTFORM',
  'SPECIES_CASTFORM_SUNNY',
  'SPECIES_CASTFORM_RAINY',
  'SPECIES_CASTFORM_SNOWY',
  'SPECIES_KECLEON',
  'SPECIES_SHUPPET',
  'SPECIES_BANETTE',
  'SPECIES_DUSKULL',
  'SPECIES_DUSCLOPS',
  'SPECIES_TROPIUS',
  'SPECIES_CHIMECHO',
  'SPECIES_ABSOL',
  'SPECIES_WYNAUT',
  'SPECIES_SNORUNT',
  'SPECIES_GLALIE',
  'SPECIES_SPHEAL',
  'SPECIES_SEALEO',
  'SPECIES_WALREIN',
  'SPECIES_CLAMPERL',
  'SPECIES_HUNTAIL',
  'SPECIES_GOREBYSS',
  'SPECIES_RELICANTH',
  'SPECIES_LUVDISC',
  'SPECIES_BAGON',
  'SPECIES_SHELGON',
  'SPECIES_SALAMENCE',
  'SPECIES_BELDUM',
  'SPECIES_METANG',
  'SPECIES_METAGROSS',
  'SPECIES_REGIROCK',
  'SPECIES_REGICE',
  'SPECIES_REGISTEEL',
  'SPECIES_LATIAS',
  'SPECIES_LATIOS',
  'SPECIES_KYOGRE',
  'SPECIES_GROUDON',
  'SPECIES_RAYQUAZA',
  'SPECIES_JIRACHI',
  'SPECIES_DEOXYS',
  'SPECIES_UNOWN_!',
  'SPECIES_UNOWN_?',
  'SPECIES_DEOXYS_ATTACK',
  'SPECIES_DEOXYS_DEFENSE',
  'SPECIES_DEOXYS_SPEED',
  'SPECIES_MUNCHLAX',
  'SPECIES_DECOY',
  'SPECIES_STATUE',
  'SPECIES_RAYQUAZA_CUTSCENE'
]

for species in species_list:
    species_map[index] = species
    index += 1

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
for i in range(0, len(splitLine), 8):
    # Slice the array in 8 chunks
    chunk = splitLine[i:i+8]
    print(chunk)

    # byte order
    # byte 0: species ID
    # byte 1: level
    # byte 2 - 3: percentage
    # byte 4 - 5: percentage
    # byte 6 - 7: always zero

    SpeciesID = chunk[0].lstrip(" 0x")

    if not SpeciesID:
        # We catch our all 0 line here and skip it
        probability_total = 0  # reset our total
        printList = True  # time to export our table
    else:
        # Sometimes overflow into next byte so check
        SpeciesTest = chunk[1].lstrip("0x")
        SpeciesTest = int(SpeciesTest, 16)
        if SpeciesTest & 1:
            SpeciesID = "1" + SpeciesID
        # print("SpeciesID HEX: {}".format(SpeciesID))
        # print("species: {}".format(int(SpeciesID, 16)))

    level = chunk[1].strip(" 0x")
    if printList:
        print("")
    else:
        if not level:
            print("level: 0")
        else:
            temp = '{:<04}'
            level = temp.format(level)
            print("LEVEL HEX: {}".format(level))
            level = int(level, 16)
            level = level / 512
            print("level: {}".format(level))

            # BUG: decoy level is messed up so hardcode to 1 so we still match
            print("TEST " + SpeciesID)
            if SpeciesID == "1a5":
                level = 1

    # Use lstrip to only strip the beginning
    # print("PERCENT DEBUG: " + chunk[3] + " " + chunk[2])
    # print("PERCENT H: " + chunk[3].lstrip("0x").zfill(2))
    # print("PERCENT L: " + chunk[2].lstrip("0x").zfill(2))

    # Zfill to get leading zero back to not fuck our percentages
    percentage = chunk[3].lstrip("0x").zfill(2) + chunk[2].lstrip("0x").zfill(2)

    # print("Pre total: {}".format(probability_total))

    if not percentage:
        print("probability: 0")
    else:
        if int(percentage, 16) == 0:
            cur_percentage = 0
        else:
            cur_percentage = int(percentage, 16) - probability_total
        # print("perobability {}".format(cur_percentage))
        probability_total += cur_percentage

    # print("Cur total: {}".format(probability_total))

    if not printList:
        pokemon_dict = {
                'species': species_map[int(SpeciesID, 16)],
                'level': int(level),
                'probability': int(cur_percentage)
        }
        floor_dict.append(pokemon_dict)
    else:
        # print(floor_dict)
        name = "pokemon_found_out" + str(num_floors)
        master_dict = {"name": name, "pokemon": floor_dict}
        with open("pokemon_found_out" + str(num_floors) + ".json", "w+") as fout:
            json.dump(master_dict, fout, indent=4, separators=(',', ': '))
        printList = False
        num_floors += 1
        master_dict = []
        floor_dict = []


file.close()