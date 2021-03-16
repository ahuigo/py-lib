import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", default="ahui", help="your name")
parser.add_argument('integers', nargs='+',)
#args = parser.parse_args()
args, unknown = parser.parse_known_args()
print(args, unknown)

