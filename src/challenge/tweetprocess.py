
# EXTERNAL PACKAGES
from functools import partial
from itertools import permutations
import sys

# INTERNAL PACKAGES
from .challibs import clean_tweets, TimeGraph

def interface(inpath, outpath):
    with open(inpath, 'r') as infile, \
         open(outpath, 'w+') as outfile:
        g = TimeGraph(60)
        for tweet in clean_tweets(infile):
            local = partial(g.addEdges, tweet['created_at'])
            tags  = sorted(set(tweet['hashtags']))
            local(*permutations(tags, 2))
            print("{0:.2f}".format(g.averate_degree()), file=outfile)


def cli_interface():
    """
    by convention it is helpful to have a wrapper_cli method that interfaces
    from commandline to function spaaaaaace.
    """
    try:
        inpath  = sys.argv[1]
        outpath = sys.argv[2]
    except:
        print("usage: {}  <inpath>  <outpath>".format(sys.argv[0]))
        sys.exit(1)
    interface(inpath, outpath)
