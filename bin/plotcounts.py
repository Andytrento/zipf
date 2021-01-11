"""
my doc
"""
import argparse
import pandas as pd


def main(args):
    df = pd.read_csv(args.infile, header=None, names=("word", "word_frequency"))
    df["rank"] = df["word_frequency"].rank(ascending=False, method="max")
    df["inverse_rank"] = 1 / df["rank"]

    ax = df.plot.scatter(
        x="word_frequency", y="rank",loglog=True, figsize=[12, 6], grid=True, xlim=args.xlim
    )
    ax.figure.savefig(args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # options for input file arg , input is csv file otherwise it's stdin
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        nargs="?",
        default="-",
        help="Input file name",
    )

    # include optional --outfile arg for the output image file name. Default
    # value is plotcounts.png
    parser.add_argument(
        "--outfile", type=str, default="plotcounts.png", help="Output file name"
    )

    # include an optional --xlim arg so that the user can change the x-axis
    # bounds
    parser.add_argument(
        "--xlim",
        type=float,
        nargs=2,
        metavar=("XMIN", "XMAX"),
        default=None,
        help="X-axis bound",
    )

    # parse.args()
    args = parser.parse_args()

    main(args)
