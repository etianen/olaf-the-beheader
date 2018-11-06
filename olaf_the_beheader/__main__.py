import argparse
import glob
from functools import partial
from itertools import chain
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
import time
import os

parser = argparse.ArgumentParser(
    prog="olaf-the-beheader",
    description="OLAF BEHEAD PUNY FILES!",
)

parser.add_argument(
    "patterns",
    metavar="PATTERN",
    type=str,
    nargs="*",
    default=["*"],
    help="a pattern of puny files to behead, defaults to all files in the current directory",
)

parser.add_argument(
    "-n",
    dest="line_count",
    default=10,
    help="number of lines to behead from puny files, defaults to 10",
)


BANNER = r"""
    ,   |\ ,__
    |\   \/   `.
    \ `-.:.     `\      _____ __    _____ _____
     `-.__ `\=====|    |     |  |  |  _  |   __|
        /=`'/   ^_\    |  |  |  |__|     |   __|
      .'   /\   .=)    |_____|_____|__|__|__|
   .-'  .'|  '-(/_|
 .'  __(  \  .'`             THE BEHEADER
/_.'`  `.  |`
         \ |
          |/
"""


def _drama(a, b):
    print(a, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(1)
    print(f" {b}")


def main():
    args = parser.parse_args()
    # Say hello.
    print(BANNER)
    # Expand all patterns into a list of filenames.
    filenames = list(chain.from_iterable(
        map(partial(glob.glob, recursive=True), map(os.path.expanduser, args.patterns))
    ))
    # Warn the user.
    time.sleep(1)
    print(f"I, OLAF, HAVE FOUND {len(filenames)} FILES TO BEHEAD!")
    time.sleep(1)
    print(f"I WILL TEAR THE FIRST {args.line_count} LINES FROM EACH!")
    print()
    time.sleep(1)
    if input("SHALL I PROCEED, MY JARL? (y/n) ").lower().strip() != "y":
        _drama("THEY SHALL BE SPARED", "FOR NOW!")
        return
    # Behead each file.
    print()
    time.sleep(1)
    print("FOR ODIN!", end="", flush=True)
    for filename in filenames:
        with open(filename, "rb") as src:
            # Discard first n lines.
            for _ in range(args.line_count):
                src.readline()
            # Open a temporary file for the truncated data.
            with NamedTemporaryFile(delete=False, dir=os.path.dirname(filename)) as dst:
                copyfileobj(src, dst)
        # Overwrite the old file with the temporary file.
        os.unlink(filename)
        os.rename(dst.name, filename)
        time.sleep(0.01)
        # Report progress.
        print("!", end="", flush=True)
    # All done!
    print("")
    print("")
    _drama("THEY HAVE BEEN", "BEHEADED!")


if __name__ == "__main__":
    main()
