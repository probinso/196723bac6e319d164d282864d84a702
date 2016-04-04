#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

# EXTERNAL PACKAGES
import argparse, argcomplete
from itertools import permutations
from functools import partial

# INTERNAL PACKAGES
from .challibs import clean_tweets, TimeGraph

def interface(inpath, outpath):
    with open(inpath, 'r') as infile, \
         open(outpath, 'w+') as outfile:
        g = TimeGraph(60)
        for tweet in clean_tweets(infile):
            local = partial(g.add, tweet['created_at'])
            tags  = sorted(set(tweet['hashtags']))

            for src, dst in permutations(tags, 2):
                local(src, dst)

            print("{0:.2f}".format(g.averate_degree()), file=outfile)

def cli_interface(arguments):
    """
    by convention it is helpful to have a wrapper_cli method that interfaces
    from commandline to function spaaaaaace.
    """
    inpath  = arguments.inpath
    outpath = arguments.outpath
    interface(inpath, outpath)


def generate_parser(parser):
    parser.add_argument('inpath', type=str,
                        help="Input file locatoin for raw tweets")

    parser.add_argument('outpath', type=str,
      help="Location to save processed tweets")

    parser.set_defaults(func=cli_interface)
    return parser
