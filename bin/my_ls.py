""" List the files in a given directory with a given suffix"""

import argparse
import glob


def main(args):
    """Run the program"""
    dir = args.dir if args.dir[-1] == "/" else args.dir + "/"
    glob_input = dir + "*." + args.suffix
    glob_output = sorted(glob.glob(glob_input))
    for item in glob_output:
        print(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dir", type=str, help="Directory")
    parser.add_argument("suffix", type=str, help="File suffix (e.g py, sh)")
    args = parser.parse_args()
    main(args)
