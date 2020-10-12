import lennpy as le

import argparse

parser = argparse.ArgumentParser(description='Lennies in the command line. Need be said more?')

parser.add_argument('emotion', default='basic', nargs='?', type=str, help='the emotion of the lenny')
parser.add_argument('-r', dest='randomized', action='store_const', default=False, const=True, help='randomized lenny face generation')
parser.add_argument('-e', '--emotions', action='store_const', default=False, const=True, help='list all available emotions')

args = parser.parse_args()

def main():
    if args.emotions:
        print("\n".join(le.emotions()))
    else:
        print(le.get(args.emotion, args.randomized))
