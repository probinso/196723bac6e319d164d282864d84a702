#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

# EXTERNAL PACKAGES
from itertools import permutations
from functools import partial
import sys

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

def cli_interface():
    """
    by convention it is helpful to have a wrapper_cli method that interfaces
    from commandline to function spaaaaaace.
    """
    inpath  =     sys.argv[1]
    outpath =     sys.argv[2]
    interface(inpath, outpath)
