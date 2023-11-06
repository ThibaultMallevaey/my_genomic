import sys
import genomic.genomic 
import argparse
import genomic.tools


def main():
    parser = argparse.ArgumentParser(
        prog="parse",
        usage="parse filename",
    )
    parser.add_argument(
          "filename",
          type=str,
    )

    arguments = parser.parse_args()
    filename = arguments.filename
    return genomic.genomic.parse(filename)

if __name__ == "__main__":
        main()


