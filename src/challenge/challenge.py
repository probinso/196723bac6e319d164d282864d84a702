#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

# EXTERNAL PACKAGES
import argparse, argcomplete
import sys

# INTERNAL PACKAGES
from . import tweetprocess


def tweetprocess_parser(subparsers):
    parser = subparsers.add_parser('rawtweet')
    tweetprocess.generate_parser(parser)
    return parser


def generate_parser(parser):
    subparsers = parser.add_subparsers(help="subcommand")
    tweetprocess_parser(subparsers)
    return parser

def main():
    parser = argparse.ArgumentParser(
        description='Data Engineering Insight Challenge Problem',
    )
    parser = generate_parser(parser)
    argcomplete.autocomplete(parser)
    arguments = parser.parse_args()

    if hasattr(arguments, 'func'):
        ret = arguments.func(arguments)
    else:
        ret = parser.print_help()
    sys.exit(ret)

if __name__ == "__main__":
    main()
