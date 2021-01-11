"""
Count the occurrence of different sentence ending.
"""
import argparse


def main(args):
    text = args.infile.read()
    for ending in [".", "?", "!"]:
        count = text.count(ending)
        print(f"Number of {ending} is {count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType("r"), help="Input file name")
    args = parser.parse_args()
    main(args)
