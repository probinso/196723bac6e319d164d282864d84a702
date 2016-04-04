#!/usr/bin/env bash

<<COMMENT
if (( $# != 2)); then
  printf "Usage: %s input_path output_path \n" "$0" >&2 ;
  exit 1;
fi;
COMMENT

python3 ./src/challenge-runner.py rawtweet ./tweet_input/tweets.txt ./tweet_output/output.txt



