import bioio
import argparse
import itertools

from bioio import logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--unmasked")
    parser.add_argument("--hardmasked")
    parser.add_argument("--softmasked")

    options = parser.parse_args()

    unmasked = open(options.unmasked, 'r')
    hardmasked = open(options.hardmasked, 'r')
    softmasked = open(options.softmasked, 'w')

    for unmaskedInfo, hardmaskedInfo in itertools.izip(bioio.fastaRead(unmasked), bioio.fastaRead(hardmasked)):
        unmaskedName, unmaskedSeq = unmaskedInfo
        hardmaskedName, hardmaskedSeq = hardmaskedInfo
        print("processing sequence: %s" % unmaskedName)
        assert unmaskedName == hardmaskedName

        softmaskedSeq = ''
        for unmaskedBase, hardmaskedBase in zip(unmaskedSeq, hardmaskedSeq):
            if unmaskedBase.upper() == hardmaskedBase.upper():
                softmaskedBase = unmaskedBase.upper()
            else:
                if not hardmaskedBase.upper() == 'N':
                    print("Warning: encountered differing base: %s %s" % (unmaskedBase, hardmaskedBase))
                softmaskedBase = unmaskedBase.lower()
            softmaskedSeq += softmaskedBase
        bioio.fastaWrite(softmasked, unmaskedName, softmaskedSeq)


if __name__ == "__main__":
    main()
        
        
