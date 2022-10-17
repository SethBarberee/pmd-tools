import json, argparse, pathlib



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('files', metavar='N', type=str, nargs='+',
                    help='json files to combine')
parser.add_argument('start', metavar='S', type=int, nargs=1,
                    help='json files to combine')
parser.add_argument('end', metavar='E', type=int, nargs=1,
                    help='json files to combine')

args = parser.parse_args()

fileList = [path for path in args.files]

# We start with 112
base = args.start[0] - 611
end = args.end[0] - 611

#print(fileList[base:end])

result = list()

for file in fileList[base:end]:
    with open(file, 'r') as f:
        result.append(json.load(f))

master_dict = {"tables": result}

with open('out.json', 'w') as output_file:
    json.dump(master_dict, output_file,indent = 4, separators=(',',': '))
#json.load()
