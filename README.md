# Solution Description

Pure Python3 solution to Insight Coding Challenge, with updated `./data-gen/get-tweets.py` for Python3 compliance.

Structures used to solve problem are described in `./src/challenge/challibs.py`. `challibs.TimeGraph` is a structure that mantains a sliding window of time for edges of a graph. This will not produce useful results against edges with timestamps occuring before the *Unix Epock*.

`challibs.clean_tweets` provides a data ellis converting raw tweets in json into simple dictionaries with only critical information.

`./run.sh` wraps `./src/challenge-runner.py`, the executable, python, CLI to the program.

# Tests
always-reset-time  : list of parsable tweets that are all 60 seconds appart
empty              : process over empty file
gradual-reset-time : list of 120 parsable tweets seperated by a second
malformed-input    : list of garbage input, treated same as limit-json entries
never-reset-time   : list of 60 parsable tweets seperated by a second
one-tweet          : simplified single tweet
time-without-edge  : update graph with new tweet that has no edge

Large test was not included, due to size. Large test had
 * 306011 lines of text pulled using `./data/get-tweets.py` (874M)
 * contained 16484 limits, which registered as malformed input
 * produced 289527 lines of text in output in 5m27.199s with trivial memory profile

## Repo directory structure

    .
    ├── data-gen
    │   ├── get-tweets.py
    │   ├── README.md
    │   └── tweets.txt
    ├── insight_testsuite
    │   ├── results.txt
    │   ├── run_tests.sh
    │   └── tests
    │       ├── always-reset-time
    │       │   └── ...
    │       ├── empty
    │       │   └── ...
    │       ├── gradual-reset-time
    │       │   └── ...
    │       ├── malformed-input
    │       │   └── ...
    │       ├── never-reset-time
    │       │   └── ...
    │       ├── one-tweet
    │       │   └── ...
    │       ├── test-2-tweets-all-distinct
    │       │   └── ...
    │       └── time-without-edge
    │           └── ...
    ├── README.md
    ├── run.sh
    ├── src
    │   ├── challenge
    │   │   ├── challibs.py
    │   │   └── tweetprocess.py
    │   └── challenge-runner.py
    ├── tweet_input
    │   └── tweets.txt -> ../data-gen/tweets.txt
    └── tweet_output
        └── output.txt


